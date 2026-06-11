#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "notes/001_from_17_to_18.md",
    "kernel/001_construction_kernel.md",
    "kernel/002_proof_kernel.md",
    "admission/001_admission_standard.md",
    "certificates/README.md",
]

missing = []
for rel in required:
    if not (ROOT / rel).exists():
        missing.append(rel)

ok = not missing

print("kernel_project_ok=" + str(ok))
print("required_count=" + str(len(required)))
print("missing_count=" + str(len(missing)))

if missing:
    print("missing:")
    for item in missing:
        print("- " + item)

raise SystemExit(0 if ok else 1)
