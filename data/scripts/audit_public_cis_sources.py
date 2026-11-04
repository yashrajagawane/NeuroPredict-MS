"""Audit the two publicly licensed CIS-to-MS source workbooks without altering them.

This script intentionally uses only the Python standard library.  It profiles
the official Mendeley workbooks, records their hashes, and emits evidence about
whether either source can support the project's longitudinal CIS-to-MS target.
It never creates patient, visit, or outcome training tables from the sources.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from html import escape
from pathlib import Path
from statistics import median
from typing import Any
from zipfile import ZipFile

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PACKAGE_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"m": MAIN_NS, "r": REL_NS, "pr": PACKAGE_REL_NS}


@dataclass(frozen=True)
class SourceSpec:
    source_id: str
    display_name: str
    raw_relative_path: Path
    data_url: str
    publication_url: str
    license_name: str
    expected_sha256: str
    header_row: int
    identifier_column: str
    outcome_column: str
    temporal_evidence: str
    outcome_interpretation: str


SOURCES = (
    SourceSpec(
        source_id="mendeley_8wk5hjx7x2_v1",
        display_name="Mexican prospective CIS cohort",
        raw_relative_path=Path("data/raw/mendeley_8wk5hjx7x2_v1/Data Base.xlsx"),
        data_url="https://doi.org/10.17632/8wk5hjx7x2.1",
        publication_url="https://doi.org/10.1016/j.arcmed.2023.102843",
        license_name="CC BY 4.0",
        expected_sha256=("070bfe92c78ef3b0bbd3169b61b8befa98c687b61322298b9143d540ae3c00d7"),
        header_row=4,
        identifier_column="Patient",
        outcome_column="group",
        temporal_evidence=(
            "The publication reports 10 years of study follow-up, but the "
            "downloadable workbook has no visit IDs, visit dates, conversion "
            "dates, last-follow-up dates, or per-visit observations."
        ),
        outcome_interpretation=(
            "The workbook's group codes are not documented in a source data "
            "dictionary. Group 1 has 125 rows, which matches the publication's "
            "125 reported conversions; this makes the mapping plausible but "
            "inferred rather than machine-readable source documentation."
        ),
    ),
    SourceSpec(
        source_id="mendeley_yjfydt34rs_v1",
        display_name="Lithuanian retrospective CIS cohort",
        raw_relative_path=Path("data/raw/mendeley_yjfydt34rs_v1/Database.xlsx"),
        data_url="https://doi.org/10.17632/yjfydt34rs.1",
        publication_url="https://doi.org/10.3390/medicina58091178",
        license_name="CC BY 4.0",
        expected_sha256=("0e9e56026c9de83c38edbe934cd93a4e44cd845507a0e844a4b3d1926e1e8880"),
        header_row=1,
        identifier_column="Nr",
        outcome_column="MS",
        temporal_evidence=(
            "The publication covers records reviewed from 2015 through 2020, "
            "but the workbook has no patient-level baseline, visit, conversion, "
            "or last-follow-up dates and no repeated visit rows."
        ),
        outcome_interpretation=(
            "The MS field is a final-diagnosis indicator with 49 positive and "
            "89 negative rows. A fixed future prediction horizon cannot be "
            "validated from the downloadable file."
        ),
    ),
)


def is_missing(value: Any) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def normalized_value(value: Any) -> str:
    if is_missing(value):
        return ""
    return str(value).strip()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def spreadsheet_column(ref: str) -> str:
    return "".join(char for char in ref if char.isalpha())


def shared_string_text(node: ET.Element) -> str:
    return "".join(text.text or "" for text in node.findall(".//m:t", NS))


def load_first_worksheet(path: Path) -> tuple[str, list[tuple[int, dict[str, Any]]]]:
    """Read the first worksheet as raw cell dictionaries keyed by Excel column."""

    with ZipFile(path) as archive:
        shared_strings: list[str] = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            shared_strings = [shared_string_text(item) for item in root.findall("m:si", NS)]

        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        relationship_targets = {
            relation.attrib["Id"]: relation.attrib["Target"]
            for relation in relationships.findall("pr:Relationship", NS)
        }
        first_sheet = workbook.find("m:sheets/m:sheet", NS)
        if first_sheet is None:
            raise ValueError(f"No worksheet found in {path}")
        relation_id = first_sheet.attrib[
            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
        ]
        target = relationship_targets[relation_id].lstrip("/")
        if not target.startswith("xl/"):
            target = f"xl/{target}"
        worksheet = ET.fromstring(archive.read(target))

        rows: list[tuple[int, dict[str, Any]]] = []
        for row in worksheet.findall("m:sheetData/m:row", NS):
            values: dict[str, Any] = {}
            for cell in row.findall("m:c", NS):
                column = spreadsheet_column(cell.attrib["r"])
                kind = cell.attrib.get("t")
                value_node = cell.find("m:v", NS)
                if kind == "inlineStr":
                    value: Any = "".join(text.text or "" for text in cell.findall(".//m:t", NS))
                elif value_node is None:
                    value = None
                elif kind == "s":
                    value = shared_strings[int(value_node.text)]
                else:
                    value = value_node.text
                values[column] = value
            rows.append((int(row.attrib["r"]), values))

    return first_sheet.attrib["name"], rows


def unique_header_fields(header: dict[str, Any]) -> dict[str, str]:
    """Preserve duplicate source headers by adding their Excel column reference."""

    counts = Counter(normalized_value(value) for value in header.values())
    result: dict[str, str] = {}
    for column, value in header.items():
        raw_name = normalized_value(value) or f"unnamed_{column}"
        result[column] = raw_name if counts[raw_name] == 1 else f"{raw_name} [{column}]"
    return result


def numeric_values(values: list[Any]) -> list[float]:
    parsed: list[float] = []
    for value in values:
        if is_missing(value):
            continue
        try:
            parsed.append(float(str(value).strip()))
        except ValueError:
            return []
    return parsed


def raw_records(
    rows: list[tuple[int, dict[str, Any]]],
    header_row: int,
    identifier_column: str,
) -> tuple[dict[str, str], list[dict[str, Any]]]:
    header_cells = next((cells for row, cells in rows if row == header_row), None)
    if header_cells is None:
        raise ValueError(f"Header row {header_row} not found")
    headers = unique_header_fields(header_cells)
    id_column = next(
        (
            column
            for column, name in headers.items()
            if normalized_value(header_cells[column]) == identifier_column
        ),
        None,
    )
    if id_column is None:
        raise ValueError(f"Identifier {identifier_column!r} not found in source header")

    records: list[dict[str, Any]] = []
    for row_number, cells in rows:
        if row_number <= header_row or is_missing(cells.get(id_column)):
            continue
        record = {"__source_row__": row_number}
        for column, field_name in headers.items():
            record[field_name] = cells.get(column)
        records.append(record)
    return headers, records


def column_summary(records: list[dict[str, Any]], field_name: str) -> dict[str, Any]:
    values = [record.get(field_name) for record in records]
    present = [value for value in values if not is_missing(value)]
    unique_values = sorted(set(normalized_value(value) for value in present))
    result: dict[str, Any] = {
        "field_name": field_name,
        "records": len(values),
        "missing_count": len(values) - len(present),
        "missing_pct": round((len(values) - len(present)) / len(values) * 100 if values else 0, 3),
        "distinct_non_missing": len(unique_values),
        "value_type_hint": "numeric" if numeric_values(present) else "categorical_or_mixed",
    }
    values_as_counts = Counter(normalized_value(value) for value in present)
    if len(values_as_counts) <= 15:
        result["value_counts"] = dict(sorted(values_as_counts.items(), key=lambda item: item[0]))
    numbers = numeric_values(present)
    if numbers:
        result["numeric_min"] = min(numbers)
        result["numeric_median"] = median(numbers)
        result["numeric_max"] = max(numbers)
    return result


def exact_duplicate_count(records: list[dict[str, Any]], field_names: list[str]) -> int:
    fingerprints = [
        tuple(normalized_value(record.get(field)) for field in field_names) for record in records
    ]
    return len(fingerprints) - len(set(fingerprints))


def find_field(records: list[dict[str, Any]], requested_name: str) -> str:
    if not records:
        raise ValueError("No data records found")
    fields = [name for name in records[0] if name != "__source_row__"]
    for field in fields:
        if field == requested_name:
            return field
    raise ValueError(f"Field {requested_name!r} was not found")


def audit_source(repo_root: Path, spec: SourceSpec) -> dict[str, Any]:
    raw_path = repo_root / spec.raw_relative_path
    if not raw_path.is_file():
        raise FileNotFoundError(
            f"Raw source is missing: {raw_path}. Acquire it from {spec.data_url}."
        )
    sheet_name, rows = load_first_worksheet(raw_path)
    headers, records = raw_records(rows, spec.header_row, spec.identifier_column)
    fields = list(headers.values())
    identifier_field = find_field(records, spec.identifier_column)
    outcome_field = find_field(records, spec.outcome_column)
    identifiers = [normalized_value(record.get(identifier_field)) for record in records]
    duplicate_identifier_count = len(identifiers) - len(set(identifiers))
    outcome_counts = Counter(normalized_value(record.get(outcome_field)) for record in records)
    column_summaries = [column_summary(records, field) for field in fields]

    date_like_fields = [
        field
        for field in fields
        if re.search(r"(date|time|month|visit|follow.?up|conversion)", field, re.I)
    ]
    return {
        "source_id": spec.source_id,
        "display_name": spec.display_name,
        "raw_file": str(spec.raw_relative_path).replace("\\", "/"),
        "data_url": spec.data_url,
        "publication_url": spec.publication_url,
        "license": spec.license_name,
        "official_sha256": spec.expected_sha256,
        "observed_sha256": sha256_file(raw_path),
        "hash_matches_official": sha256_file(raw_path).lower() == spec.expected_sha256.lower(),
        "file_size_bytes": raw_path.stat().st_size,
        "worksheet": sheet_name,
        "header_row": spec.header_row,
        "source_row_count_with_identifier": len(records),
        "source_column_count": len(fields),
        "source_columns": [
            {
                "excel_column": column,
                "raw_source_header": normalized_value(
                    next(cells[column] for row, cells in rows if row == spec.header_row)
                ),
                "audit_field_name": field_name,
            }
            for column, field_name in headers.items()
        ],
        "identifier": {
            "source_column": identifier_field,
            "unique_non_missing_count": len(set(identifiers)),
            "duplicate_identifier_count": duplicate_identifier_count,
            "exact_duplicate_row_count": exact_duplicate_count(records, fields),
        },
        "outcome": {
            "source_column": outcome_field,
            "raw_value_counts": dict(sorted(outcome_counts.items(), key=lambda item: item[0])),
            "interpretation": spec.outcome_interpretation,
        },
        "candidate_temporal_fields": date_like_fields,
        "temporal_evidence": spec.temporal_evidence,
        "has_patient_linked_repeated_visits": False,
        "has_visit_dates": False,
        "has_conversion_dates": False,
        "has_last_follow_up_dates": False,
        "can_support_final_longitudinal_rnn_lstm_dataset": False,
        "column_summaries": column_summaries,
    }


def write_missingness_report(audits: list[dict[str, Any]], output_path: Path) -> None:
    rows: list[dict[str, Any]] = []
    for audit in audits:
        for column in audit["column_summaries"]:
            rows.append(
                {
                    "source_dataset": audit["source_id"],
                    "source_column": column["field_name"],
                    "records": column["records"],
                    "missing_count": column["missing_count"],
                    "missing_pct": column["missing_pct"],
                    "distinct_non_missing": column["distinct_non_missing"],
                    "value_type_hint": column["value_type_hint"],
                }
            )
    fieldnames = list(rows[0]) if rows else []
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_cohort_size_svg(audits: list[dict[str, Any]], output_path: Path) -> None:
    """Create a dependency-free chart of raw candidate rows and the 2,000 goal."""

    items = [
        ("Mexican public workbook", audits[0]["source_row_count_with_identifier"]),
        ("Lithuanian public workbook", audits[1]["source_row_count_with_identifier"]),
        ("Aspirational target", 2000),
    ]
    max_value = max(value for _, value in items)
    width, height = 940, 330
    chart_left, chart_top, chart_width, chart_height = 255, 70, 610, 170
    colors = ["#527da4", "#6f9e88", "#a16b55"]
    bar_height, gap = 38, 18
    bars: list[str] = []
    for index, ((label, value), color) in enumerate(zip(items, colors)):
        y = chart_top + index * (bar_height + gap)
        bar_width = chart_width * value / max_value
        bars.append(
            f'<text x="32" y="{y + 25}" font-size="16" fill="#1e293b">{escape(label)}</text>'
        )
        bars.append(
            f'<rect x="{chart_left}" y="{y}" width="{bar_width:.1f}" '
            f'height="{bar_height}" fill="{color}" />'
        )
        bars.append(
            f'<text x="{chart_left + bar_width + 10:.1f}" y="{y + 25}" '
            f'font-size="16" fill="#1e293b">{value:,}</text>'
        )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">Public candidate cohort rows compared with the 2,000-patient aspiration</title>
  <desc id="desc">The Mexican workbook has 273 rows, the Lithuanian workbook has 138 rows, and the aspirational cohort size is 2,000. These are raw source rows, not an approved longitudinal training cohort.</desc>
  <rect width="100%" height="100%" fill="#ffffff"/>
  <text x="32" y="34" font-family="Arial, sans-serif" font-size="20" font-weight="700" fill="#0f172a">Public candidate rows remain far below the 2,000-patient aspiration</text>
  <text x="32" y="58" font-family="Arial, sans-serif" font-size="13" fill="#475569">Source: official Mendeley workbooks downloaded 2026-11-04. Counts are raw rows, not approved longitudinal model cohorts.</text>
  {"".join(bars)}
  <line x1="{chart_left}" y1="{chart_top + chart_height + 16}" x2="{chart_left + chart_width}" y2="{chart_top + chart_height + 16}" stroke="#94a3b8" stroke-width="1"/>
  <text x="{chart_left}" y="{chart_top + chart_height + 40}" font-family="Arial, sans-serif" font-size="13" fill="#475569">Patient rows (count)</text>
</svg>
'''
    output_path.write_text(svg, encoding="utf-8")


def write_manifest(audits: list[dict[str, Any]], output_path: Path) -> None:
    manifest = {
        "manifest_version": "1.0",
        "generated_at_utc": datetime.now(UTC).isoformat(),
        "intended_prediction_task": (
            "Future conversion from confirmed baseline CIS to MS within a defined "
            "post-index horizon."
        ),
        "dataset_readiness": "NO_GO",
        "dataset_ready_for_hybrid_rnn_lstm_training": False,
        "stop_conditions_triggered": [
            "No public candidate has patient-linked repeated visit records.",
            "No public candidate has patient-level index, conversion, and last-follow-up dates.",
            "The intended outcome horizon cannot be validated from the downloaded files.",
        ],
        "public_source_audits": audits,
        "not_created": {
            "patients_csv": "No eligible final longitudinal cohort is available.",
            "visits_csv": "No genuine visit-level records with dates are present.",
            "outcomes_csv": "No patient-level index/conversion/last-follow-up dates are present.",
        },
    }
    output_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def run(repo_root: Path, output_dir: Path) -> list[dict[str, Any]]:
    audits = [audit_source(repo_root, spec) for spec in SOURCES]
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "public_source_audit.json").write_text(
        json.dumps(
            {
                "generated_at_utc": datetime.now(UTC).isoformat(),
                "sources": audits,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    write_missingness_report(audits, output_dir / "missingness_report.csv")
    write_cohort_size_svg(audits, output_dir / "public_candidate_cohort_sizes.svg")
    write_manifest(audits, output_dir / "dataset_manifest.json")
    return audits


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit official public CIS-to-MS Mendeley source workbooks."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Repository root containing data/raw.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory for non-patient-level audit outputs.",
    )
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    output_dir = args.output_dir.resolve() if args.output_dir else repo_root / "data" / "audit"
    audits = run(repo_root, output_dir)
    for audit in audits:
        print(
            f"{audit['source_id']}: rows={audit['source_row_count_with_identifier']}, "
            f"unique_ids={audit['identifier']['unique_non_missing_count']}, "
            f"outcome_counts={audit['outcome']['raw_value_counts']}, "
            f"hash_ok={audit['hash_matches_official']}"
        )
    print(f"Wrote audit outputs to {output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
