#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STATUS = ROOT / "artifacts/json/construction_independence_status.json"
NOTE = ROOT / "notes/002_construction_independence.md"
OUT = ROOT / "artifacts/md/construction_independence_verification.md"

def csv_row_count(path):
    with path.open() as f:
        return max(0, sum(1 for _ in f) - 1)

def main():
    data = json.loads(STATUS.read_text())

    payload_paths = [ROOT / p for p in data["kernel_payload"]]
    payload_exists = [p.exists() for p in payload_paths]

    expected_rows = {
        "source/kernel_payload/g15_slot_edges.csv": 30,
        "source/kernel_payload/g60_local_edges.csv": 120,
        "source/kernel_payload/carrier_signing_table.csv": 30,
        "source/kernel_payload/x_sigma_edges.csv": 3600,
    }

    row_checks = {}
    for rel, expected in expected_rows.items():
        path = ROOT / rel
        row_checks[rel] = path.exists() and csv_row_count(path) == expected

    checks = {
        "status_exists": STATUS.exists(),
        "note_exists": NOTE.exists(),
        "construction_independent_flag": data.get("construction_independent_of_project17") is True,
        "qed_independent_flag_false": data.get("qed_independent") is False,
        "all_payload_files_exist": all(payload_exists),
        "payload_row_counts_ok": all(row_checks.values()),
        "remaining_certificate_targets_count": len(data.get("remaining_certificate_targets", [])) == 7,
        "source_role_is_provenance": data.get("source_role") == "frozen provenance checkpoint",
    }

    ok = all(checks.values())

    lines = []
    lines.append("# Construction independence verification")
    lines.append("")
    lines.append("- verification_ok: " + str(ok))
    lines.append("- construction_independent_of_project17: " + str(data.get("construction_independent_of_project17")))
    lines.append("- qed_independent: " + str(data.get("qed_independent")))
    lines.append("")
    lines.append("## Payload row checks")
    lines.append("")
    for rel, result in row_checks.items():
        lines.append("- " + rel + ": " + str(result))
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in checks.items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")

    OUT.write_text("\n".join(lines))

    print("construction_independence_verification_ok=" + str(ok))
    print("wrote", OUT)

    if not ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
