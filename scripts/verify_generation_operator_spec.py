#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "artifacts/json/generation_operator_spec.json"
MD = ROOT / "kernel/003_generation_operator.md"
OUT = ROOT / "artifacts/md/generation_operator_verification.md"

def main():
    spec = json.loads(SPEC.read_text())

    checks = {
        "spec_exists": SPEC.exists(),
        "markdown_exists": MD.exists(),
        "operator_is_Gen": spec.get("operator") == "Gen",
        "input_kernel_is_K_900": spec.get("input_kernel") == "K_900",
        "output_graph_is_X_sigma": spec.get("output_graph") == "X_sigma",
        "has_four_kernel_components": spec.get("kernel_components") == ["G15", "G60", "sigma", "h"],
        "G15_counts_ok": spec["inputs"]["G15"]["vertex_count"] == 15 and spec["inputs"]["G15"]["edge_count"] == 30,
        "G60_counts_ok": spec["inputs"]["G60"]["vertex_count"] == 60 and spec["inputs"]["G60"]["edge_count"] == 120,
        "generated_vertex_count_ok": spec.get("generated_vertex_count") == 900,
        "internal_edge_count_ok": spec["edge_layers"]["internal"]["edge_count"] == 1800,
        "carrier_edge_count_ok": spec["edge_layers"]["carrier"]["edge_count"] == 1800,
        "generated_edge_count_ok": spec.get("generated_edge_count") == 3600,
        "deterministic": spec.get("deterministic") is True
    }

    ok = all(checks.values())

    lines = []
    lines.append("# Generation operator verification")
    lines.append("")
    lines.append("- verification_ok: " + str(ok))
    lines.append("- checked_spec: artifacts/json/generation_operator_spec.json")
    lines.append("- checked_note: kernel/003_generation_operator.md")
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in checks.items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")

    OUT.write_text("\n".join(lines))

    print("generation_operator_verification_ok=" + str(ok))
    print("wrote", OUT)

    if not ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
