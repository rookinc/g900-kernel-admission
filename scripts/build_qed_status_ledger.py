#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXACT = ROOT / "artifacts/json/exact_edge_set_identity_certificate.json"
CONN = ROOT / "artifacts/json/connectedness_certificate.json"
METRIC = ROOT / "artifacts/json/metric_certificate.json"

OUT_JSON = ROOT / "artifacts/json/qed_status_ledger.json"
OUT_MD = ROOT / "admission/003_qed_status_ledger.md"
OUT_VERIFY = ROOT / "artifacts/md/qed_status_ledger_verification.md"

def read_json(path):
    if not path.exists():
        return None
    return json.loads(path.read_text())

def main():
    exact = read_json(EXACT)
    conn = read_json(CONN)
    metric = read_json(METRIC)

    exact_ok = bool(exact and exact.get("verification_ok") is True)
    conn_ok = bool(conn and conn.get("verification_ok") is True)
    metric_ok = bool(metric and metric.get("verification_ok") is True)

    diameter_ok = bool(metric_ok and metric.get("diameter") == 8)
    radius_ok = bool(metric_ok and metric.get("radius") == 6)

    claims = [
        {
            "id": "product_register_size",
            "status": "proved_by_kernel",
            "support": "finite product count |V15| * |V60| = 15 * 60 = 900"
        },
        {
            "id": "internal_edge_count",
            "status": "proved_by_kernel",
            "support": "15 copies of 120 G60 edges gives 1800 internal edges"
        },
        {
            "id": "external_edge_count",
            "status": "proved_by_kernel",
            "support": "30 slot edges times 60 carrier states gives 1800 external edges"
        },
        {
            "id": "total_edge_count",
            "status": "proved_by_kernel",
            "support": "1800 internal + 1800 external = 3600 total edges"
        },
        {
            "id": "degree_split",
            "status": "proved_by_kernel",
            "support": "4 internal neighbors plus 4 external carrier neighbors"
        },
        {
            "id": "regularity",
            "status": "proved_by_kernel",
            "support": "degree split gives 8-regularity"
        },
        {
            "id": "exact_edge_set_identity",
            "status": "certified" if exact_ok else "not_certified",
            "support": "artifacts/json/exact_edge_set_identity_certificate.json",
            "verification_ok": exact_ok
        },
        {
            "id": "connectedness",
            "status": "certified" if conn_ok else "not_certified",
            "support": "artifacts/json/connectedness_certificate.json",
            "verification_ok": conn_ok
        },
        {
            "id": "diameter",
            "status": "certified" if diameter_ok else "not_certified",
            "support": "artifacts/json/metric_certificate.json",
            "verification_ok": diameter_ok,
            "value": metric.get("diameter") if metric else None
        },
        {
            "id": "radius",
            "status": "certified" if radius_ok else "not_certified",
            "support": "artifacts/json/metric_certificate.json",
            "verification_ok": radius_ok,
            "value": metric.get("radius") if metric else None
        },
        {
            "id": "baseline_separation",
            "status": "planned",
            "support": "needs baseline metric certificate internal to Project 18"
        },
        {
            "id": "sibling_non_switching",
            "status": "planned",
            "support": "needs F2 coboundary obstruction certificate internal to Project 18"
        },
        {
            "id": "sibling_full_graph_separation",
            "status": "planned",
            "support": "needs exact invariant separation certificate internal to Project 18"
        }
    ]

    status_counts = {}
    for claim in claims:
        status_counts[claim["status"]] = status_counts.get(claim["status"], 0) + 1

    certified_ids = [c["id"] for c in claims if c["status"] == "certified"]
    proved_ids = [c["id"] for c in claims if c["status"] == "proved_by_kernel"]
    planned_ids = [c["id"] for c in claims if c["status"] == "planned"]

    verification_checks = {
        "exact_edge_set_identity_certified": exact_ok,
        "connectedness_certified": conn_ok,
        "diameter_certified": diameter_ok,
        "radius_certified": radius_ok,
        "direct_kernel_proof_count_is_6": len(proved_ids) == 6,
        "planned_remaining_count_is_3": len(planned_ids) == 3
    }

    ledger_ok = all(verification_checks.values())

    ledger = {
        "project": "18-g900-kernel-admission",
        "ledger": "qed_status_ledger",
        "ledger_ok": ledger_ok,
        "claims": claims,
        "status_counts": status_counts,
        "proved_by_kernel": proved_ids,
        "certified": certified_ids,
        "planned": planned_ids,
        "verification_checks": verification_checks,
        "current_summary": {
            "direct_kernel_claims_proved": len(proved_ids),
            "certificate_claims_certified": len(certified_ids),
            "remaining_planned_claims": len(planned_ids),
            "qed_complete": False
        },
        "boundary": [
            "This is a status overlay, not a replacement for the claim ledger.",
            "QED is not complete until the remaining planned claims are certified or removed from the theorem.",
            "No uniqueness, census identity, physical interpretation, or sibling invalidity is claimed."
        ]
    }

    OUT_JSON.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n")

    lines = []
    lines.append("# QED status ledger")
    lines.append("")
    lines.append("- ledger_ok: " + str(ledger_ok))
    lines.append("- direct_kernel_claims_proved: " + str(len(proved_ids)))
    lines.append("- certificate_claims_certified: " + str(len(certified_ids)))
    lines.append("- remaining_planned_claims: " + str(len(planned_ids)))
    lines.append("- qed_complete: False")
    lines.append("")
    lines.append("## Proved by kernel")
    lines.append("")
    for item in proved_ids:
        lines.append("- " + item)
    lines.append("")
    lines.append("## Certified")
    lines.append("")
    for item in certified_ids:
        lines.append("- " + item)
    lines.append("")
    lines.append("## Planned")
    lines.append("")
    for item in planned_ids:
        lines.append("- " + item)
    lines.append("")
    lines.append("## Claim table")
    lines.append("")
    for claim in claims:
        lines.append("- " + claim["id"] + ": " + claim["status"])
        lines.append("  - support: " + str(claim.get("support")))
        if "value" in claim:
            lines.append("  - value: " + str(claim.get("value")))
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    for b in ledger["boundary"]:
        lines.append("- " + b)
    lines.append("")

    OUT_MD.write_text("\n".join(lines))

    verify_lines = []
    verify_lines.append("# QED status ledger verification")
    verify_lines.append("")
    verify_lines.append("- verification_ok: " + str(ledger_ok))
    verify_lines.append("")
    verify_lines.append("## Checks")
    verify_lines.append("")
    for k, v in verification_checks.items():
        verify_lines.append("- " + k + ": " + str(v))
    verify_lines.append("")
    verify_lines.append("## Status counts")
    verify_lines.append("")
    for k in sorted(status_counts):
        verify_lines.append("- " + k + ": " + str(status_counts[k]))
    verify_lines.append("")

    OUT_VERIFY.write_text("\n".join(verify_lines))

    print("qed_status_ledger_ok=" + str(ledger_ok))
    print("proved_by_kernel_count=" + str(len(proved_ids)))
    print("certified_count=" + str(len(certified_ids)))
    print("planned_count=" + str(len(planned_ids)))
    print("certified=" + ",".join(certified_ids))
    print("planned=" + ",".join(planned_ids))
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)
    print("wrote", OUT_VERIFY)

    if not ledger_ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
