#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "artifacts/json/kernel_claim_ledger.json"
NOTE = ROOT / "admission/002_kernel_claim_ledger.md"
OUT = ROOT / "artifacts/md/kernel_claim_ledger_verification.md"

REQUIRED_CLASSES = [
    "direct_proof",
    "certificate_required",
    "external_boundary",
    "not_claimed",
]

REQUIRED_DIRECT = [
    "product_register_size",
    "internal_edge_count",
    "external_edge_count",
    "total_edge_count",
    "degree_split",
    "regularity",
]

REQUIRED_CERT = [
    "connectedness",
    "diameter",
    "radius",
    "exact_edge_set_identity",
    "sibling_non_switching",
    "sibling_full_graph_separation",
]

REQUIRED_BOUNDARY = [
    "census_identification",
    "uniqueness",
    "physical_interpretation",
]

def ids(rows):
    return [r.get("id") for r in rows]

def main():
    data = json.loads(LEDGER.read_text())

    direct_ids = ids(data.get("direct_proof", []))
    cert_ids = ids(data.get("certificate_required", []))
    boundary_ids = ids(data.get("external_boundary", []))

    checks = {
        "ledger_exists": LEDGER.exists(),
        "note_exists": NOTE.exists(),
        "claim_classes_ok": data.get("claim_classes") == REQUIRED_CLASSES,
        "direct_claims_complete": direct_ids == REQUIRED_DIRECT,
        "certificate_claims_complete": cert_ids == REQUIRED_CERT,
        "boundary_claims_complete": boundary_ids == REQUIRED_BOUNDARY,
        "has_not_claimed_list": len(data.get("not_claimed", [])) >= 5,
        "has_admission_principle": bool(data.get("admission_principle")),
    }

    ok = all(checks.values())

    lines = []
    lines.append("# Kernel claim ledger verification")
    lines.append("")
    lines.append("- verification_ok: " + str(ok))
    lines.append("- checked_ledger: artifacts/json/kernel_claim_ledger.json")
    lines.append("- checked_note: admission/002_kernel_claim_ledger.md")
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in checks.items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")
    lines.append("## Counts")
    lines.append("")
    lines.append("- direct_proof_count: " + str(len(direct_ids)))
    lines.append("- certificate_required_count: " + str(len(cert_ids)))
    lines.append("- external_boundary_count: " + str(len(boundary_ids)))
    lines.append("- not_claimed_count: " + str(len(data.get("not_claimed", []))))
    lines.append("")

    OUT.write_text("\n".join(lines))

    print("kernel_claim_ledger_verification_ok=" + str(ok))
    print("direct_proof_count=" + str(len(direct_ids)))
    print("certificate_required_count=" + str(len(cert_ids)))
    print("external_boundary_count=" + str(len(boundary_ids)))
    print("wrote", OUT)

    if not ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
