#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SET_NOTE = ROOT / "notes/003_finite_set_theoretic_floor.md"
ALG_NOTE = ROOT / "kernel/004_algebraic_kernel.md"
SPEC = ROOT / "artifacts/json/algebraic_kernel_spec.json"
OUT = ROOT / "artifacts/md/algebraic_kernel_verification.md"

def main():
    data = json.loads(SPEC.read_text())

    checks = {
        "set_note_exists": SET_NOTE.exists(),
        "algebraic_note_exists": ALG_NOTE.exists(),
        "spec_exists": SPEC.exists(),
        "foundation_is_finite_set_theory": data.get("foundation") == "finite set theory",
        "has_A15": "A15" in data.get("matrices", {}),
        "has_A60": "A60" in data.get("matrices", {}),
        "has_H": "H" in data.get("matrices", {}),
        "half_flip_rule_ok": data.get("half_flip_rule") == "h(x) = x + 30 mod 60",
        "generated_adjacency_defined": data.get("generated_adjacency") == "AX = A_internal + A_carrier",
        "direct_claim_count_ok": len(data.get("direct_algebraic_claims", [])) == 5,
        "boolean_claim_count_ok": len(data.get("boolean_reachability_claims", [])) == 3,
        "f2_claim_count_ok": len(data.get("f2_claims", [])) == 1,
        "exact_comparison_count_ok": len(data.get("exact_comparison_claims", [])) == 3,
        "non_foundational_inputs_count_ok": len(data.get("non_foundational_inputs", [])) == 6
    }

    ok = all(checks.values())

    lines = []
    lines.append("# Algebraic kernel verification")
    lines.append("")
    lines.append("- verification_ok: " + str(ok))
    lines.append("- checked_set_note: notes/003_finite_set_theoretic_floor.md")
    lines.append("- checked_algebraic_note: kernel/004_algebraic_kernel.md")
    lines.append("- checked_spec: artifacts/json/algebraic_kernel_spec.json")
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in checks.items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")

    OUT.write_text("\n".join(lines))

    print("algebraic_kernel_verification_ok=" + str(ok))
    print("wrote", OUT)

    if not ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
