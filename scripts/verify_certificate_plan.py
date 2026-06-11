#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "artifacts/json/certificate_plan.json"
NOTE = ROOT / "certificates/001_certificate_plan.md"
OUT = ROOT / "artifacts/md/certificate_plan_verification.md"

EXPECTED = [
    "connectedness",
    "diameter",
    "radius",
    "exact_edge_set_identity",
    "sibling_non_switching",
    "sibling_full_graph_separation",
    "baseline_separation",
]

def main():
    data = json.loads(PLAN.read_text())
    ids = [row.get("id") for row in data.get("certificates", [])]

    checks = {
        "plan_exists": PLAN.exists(),
        "note_exists": NOTE.exists(),
        "certificate_ids_ok": ids == EXPECTED,
        "certificate_count_ok": len(ids) == 7,
        "all_status_planned": all(row.get("status") == "planned" for row in data.get("certificates", [])),
        "has_admission_rule": bool(data.get("admission_rule")),
        "has_minimal_bounded_qed_package": len(data.get("minimal_bounded_qed_package", [])) == 7
    }

    ok = all(checks.values())

    lines = []
    lines.append("# Certificate plan verification")
    lines.append("")
    lines.append("- verification_ok: " + str(ok))
    lines.append("- certificate_count: " + str(len(ids)))
    lines.append("")
    lines.append("## Certificates")
    lines.append("")
    for item in ids:
        lines.append("- " + str(item))
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in checks.items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")

    OUT.write_text("\n".join(lines))

    print("certificate_plan_verification_ok=" + str(ok))
    print("certificate_count=" + str(len(ids)))
    print("wrote", OUT)

    if not ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
