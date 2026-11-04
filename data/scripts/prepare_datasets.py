"""Prepare existing source-preserving interim files or audit future CSV tables.

Without --source-workbooks this command runs the existing public source
extractor. It never creates longitudinal table files. To validate approved
longitudinal files, use validate_datasets.py with explicit approval flags.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from prepare_interim_cis_datasets import run as prepare_interim


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--source-workbooks", action="store_true", help="Read the two already acquired official XLSX files.")
    args = parser.parse_args()
    if not args.source_workbooks:
        parser.error("No source mode selected. Use --source-workbooks to regenerate the separate interim extracts.")
    output = args.output_dir or args.repo_root / "data" / "processed" / "interim"
    result = prepare_interim(args.repo_root.resolve(), output.resolve())
    print(f"status={result['overall_status']}")
    print("No longitudinal patients/visits/outcomes tables were created.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
