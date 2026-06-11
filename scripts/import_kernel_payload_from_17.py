#!/usr/bin/env python3
import csv
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT.parent / "17-g900-theorem-proof"

OUT_DIR = ROOT / "source/kernel_payload"
OUT_JSON = ROOT / "artifacts/json/kernel_payload_manifest.json"
OUT_MD = ROOT / "artifacts/md/kernel_payload_manifest.md"

FILES = [
    {
        "role": "G15 slot edge list",
        "src": "support/admission/admitted_g15_slot_edges.csv",
        "dst": "g15_slot_edges.csv",
        "expected_rows": 30
    },
    {
        "role": "G60 local edge list",
        "src": "support/admission/admitted_g60_local_edges.csv",
        "dst": "g60_local_edges.csv",
        "expected_rows": 120
    },
    {
        "role": "carrier signing table",
        "src": "support/admission/carrier_signing_table.csv",
        "dst": "carrier_signing_table.csv",
        "expected_rows": 30
    },
    {
        "role": "regenerated X_sigma edge list",
        "src": "support/admission/regenerated_x_sigma_edges.csv",
        "dst": "x_sigma_edges.csv",
        "expected_rows": 3600
    }
]

def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def count_csv_rows(path):
    with path.open(newline="") as f:
        return sum(1 for _ in csv.DictReader(f))

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    records = []
    missing = []

    for item in FILES:
        src = SRC / item["src"]
        dst = OUT_DIR / item["dst"]

        if not src.exists():
            missing.append(item["src"])
            continue

        shutil.copy2(src, dst)
        row_count = count_csv_rows(dst)
        ok = row_count == item["expected_rows"]

        records.append({
            "role": item["role"],
            "source_path": item["src"],
            "payload_path": str(dst.relative_to(ROOT)),
            "expected_rows": item["expected_rows"],
            "row_count": row_count,
            "row_count_ok": ok,
            "sha256": sha256_file(dst),
            "bytes": dst.stat().st_size
        })

    manifest = {
        "project": "18-g900-kernel-admission",
        "source_project": "17-g900-theorem-proof",
        "purpose": "Self-contained minimal finite kernel payload for Project 18.",
        "kernel_payload_independent_of_project17": len(missing) == 0 and all(r["row_count_ok"] for r in records),
        "records": records,
        "missing": missing,
        "boundary": [
            "This payload makes the construction kernel data available inside Project 18.",
            "Project 17 remains provenance, not a runtime dependency, after this import.",
            "This does not yet create the full proof-kernel certificate bundle."
        ]
    }

    OUT_JSON.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    lines = []
    lines.append("# Kernel payload manifest")
    lines.append("")
    lines.append("- project: 18-g900-kernel-admission")
    lines.append("- source_project: 17-g900-theorem-proof")
    lines.append("- kernel_payload_independent_of_project17: " + str(manifest["kernel_payload_independent_of_project17"]))
    lines.append("- missing_count: " + str(len(missing)))
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    for b in manifest["boundary"]:
        lines.append("- " + b)
    lines.append("")
    lines.append("## Payload files")
    lines.append("")
    for r in records:
        lines.append("- " + r["role"])
        lines.append("  - payload_path: " + r["payload_path"])
        lines.append("  - source_path: " + r["source_path"])
        lines.append("  - row_count: " + str(r["row_count"]))
        lines.append("  - expected_rows: " + str(r["expected_rows"]))
        lines.append("  - row_count_ok: " + str(r["row_count_ok"]))
        lines.append("  - sha256: " + r["sha256"])
        lines.append("  - bytes: " + str(r["bytes"]))
    if missing:
        lines.append("")
        lines.append("## Missing")
        lines.append("")
        for m in missing:
            lines.append("- " + m)

    OUT_MD.write_text("\n".join(lines) + "\n")

    print("kernel_payload_independent_of_project17=" + str(manifest["kernel_payload_independent_of_project17"]))
    print("records=" + str(len(records)))
    print("missing=" + str(len(missing)))
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)

    if missing or not all(r["row_count_ok"] for r in records):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
