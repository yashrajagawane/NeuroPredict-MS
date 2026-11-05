import { readFileSync } from "node:fs";
import { resolve } from "node:path";

const stylesheet = readFileSync(resolve("src/index.css"), "utf8");

function themeColor(name) {
  const match = stylesheet.match(new RegExp(`--${name}:\\s*(#[0-9a-fA-F]{6})`));
  if (!match) throw new Error(`Theme token --${name} must be a six-digit hex color.`);
  return match[1].toLowerCase();
}

function relativeLuminance(hex) {
  const channels = hex.match(/[0-9a-f]{2}/gi);
  if (!channels) throw new Error(`Invalid hex color: ${hex}`);
  const [red, green, blue] = channels.map((channel) => {
    const value = Number.parseInt(channel, 16) / 255;
    return value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4;
  });
  if (red === undefined || green === undefined || blue === undefined) {
    throw new Error(`Invalid hex color: ${hex}`);
  }
  return 0.2126 * red + 0.7152 * green + 0.0722 * blue;
}

function contrastRatio(foreground, background) {
  const luminances = [relativeLuminance(foreground), relativeLuminance(background)].sort(
    (left, right) => right - left,
  );
  const [lighter, darker] = luminances;
  if (lighter === undefined || darker === undefined) throw new Error("Contrast calculation failed.");
  return (lighter + 0.05) / (darker + 0.05);
}

const checks = [
  { label: "main text on canvas", foreground: "foreground", background: "background", minimum: 4.5 },
  {
    label: "secondary text on canvas",
    foreground: "muted-foreground",
    background: "background",
    minimum: 4.5,
  },
  { label: "links on canvas", foreground: "primary", background: "background", minimum: 4.5 },
  { label: "active navigation text", foreground: "primary", background: "primary-quiet", minimum: 4.5 },
  { label: "primary button text", foreground: "primary-foreground", background: "primary", minimum: 4.5 },
  { label: "focus indicator on surface", foreground: "focus", background: "surface", minimum: 3 },
];

let failed = false;
for (const check of checks) {
  const ratio = contrastRatio(themeColor(check.foreground), themeColor(check.background));
  const passes = ratio >= check.minimum;
  console.log(`${passes ? "PASS" : "FAIL"} ${check.label}: ${ratio.toFixed(2)}:1 (minimum ${check.minimum}:1)`);
  if (!passes) failed = true;
}

if (failed) process.exitCode = 1;
