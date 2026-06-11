#!/usr/bin/env python3
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT.parent / "17-g900-theorem-proof"

OUT_JSON = ROOT / "source/project17_checkpoint_manifest.json"
OUT_MD = ROOT / "source/project17_checkpoint_manifest.md"

TRACKED_FILES = [
    "README.md",
    "paper/main.tex",
    "paper/sections/04_finite_lemmas.tex",
    "paper/sections/05_main_theorem.tex",
    "paper/sections/10_admission_reproducibility_summary.tex",
    "paper/sections/11_sibling_variant.tex",
    "paper/sections/12_boundary_and_next_steps.tex",
    "paper/sections/appendix_source_object_admission.tex",
    "paper/sections/appendix_carrier_law_admission.tex",
    "paper/sections/appendix_generated_graph_reproducibility.tex",
    "paper/sections/appendix_admission_spine_verification.tex",
    "paper/sections/appendix_receipts_and_source_map.tex",
    "dist/g900_theorem_proof_package_overleaf.zip",
]

def run_git(args):
    return subprocess.check_output(
        ["git", "-C", str(SRC)] + args,
        text=True,
    ).strip()

def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    if not SRC.exists():
        raise SystemExit("missing source project: " + str(SRC))

    commit = run_git(["rev-parse", "HEAD"])
    branch = run_git(["branch", "--show-current"])

    try:
        tags = run_git(["tag", "--points-at", "HEAD"]).splitlines()
    except subprocess.CalledProcessError:
        tags = []

    status = run_git(["status", "--short"])

    files = []
    missing = []
    for rel in TRACKED_FILES:
        path = SRC / rel
        if path.exists():
            files.append({
                "path": rel,
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            })
        else:
            missing.append(rel)

    manifest = {
        "source_project": "17-g900-theorem-proof",
        "source_path": str(SRC),
        "source_commit": commit,
        "source_branch": branch,
        "source_tags_at_head": tags,
        "source_worktree_clean": status == "",
        "source_status_short": status,
        "tracked_file_count": len(files),
        "missing_file_count": len(missing),
        "tracked_files": files,
        "missing_files": missing,
        "admission_use": "Frozen source checkpoint for Project 18 kernel admission.",
        "boundary": [
            "Project 18 does not modify Project 17.",
            "Project 18 studies kernel admission for the object frozen in Project 17.",
            "This manifest is a pointer and hash record, not a new theorem claim."
        ],
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    lines = []
    lines.append("# Project 17 checkpoint manifest")
    lines.append("")
    lines.append("- source_project: 17-g900-theorem-proof")
    lines.append("- source_commit: " + commit)
    lines.append("- source_branch: " + branch)
    lines.append("- source_worktree_clean: " + str(status == ""))
    lines.append("- source_tags_at_head: " + (", ".join(tags) if tags else "none"))
    lines.append("- tracked_file_count: " + str(len(files)))
    lines.append("- missing_file_count: " + str(len(missing)))
    lines.append("")
    lines.append("## Admission use")
    lines.append("")
    lines.append("Frozen source checkpoint for Project 18 kernel admission.")
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    for item in manifest["boundary"]:
        lines.append("- " + item)
    lines.append("")
    lines.append("## Tracked files")
    lines.append("")
    for item in files:
        lines.append("- " + item["path"])
        lines.append("  - sha256: " + item["sha256"])
        lines.append("  - bytes: " + str(item["bytes"]))
    if missing:
        lines.append("")
        lines.append("## Missing files")
        lines.append("")
        for rel in missing:
            lines.append("- " + rel)

    OUT_MD.write_text("\n".join(lines) + "\n")

    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)
    print("source_commit=" + commit)
    print("source_tags_at_head=" + (",".join(tags) if tags else "none"))
    print("source_worktree_clean=" + str(status == ""))
    print("tracked_file_count=" + str(len(files)))
    print("missing_file_count=" + str(len(missing)))

if __name__ == "__main__":
    main()
