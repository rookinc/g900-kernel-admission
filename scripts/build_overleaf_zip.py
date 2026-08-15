#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
DIST = ROOT / "dist"
OUT = DIST / "g900_kernel_admission_bounded_qed_overleaf.zip"

REQUIRED = [
    PAPER / "main.tex",
    PAPER / "refs.bib",
    PAPER / "sections",
]

def should_include(path: Path) -> bool:
    if path.is_dir():
        return False
    name = path.name
    if name.startswith("."):
        return False
    if name.endswith((
        ".aux", ".bbl", ".bcf", ".blg", ".fdb_latexmk", ".fls",
        ".log", ".out", ".run.xml", ".synctex.gz", ".toc"
    )):
        return False
    return True

def main():
    for path in REQUIRED:
        if not path.exists():
            raise SystemExit(f"missing required paper input: {path}")

    DIST.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as td:
        staging = Path(td) / "overleaf"
        staging.mkdir(parents=True, exist_ok=True)

        # Overleaf works best when main.tex is at the zip root.
        for item in PAPER.iterdir():
            if item.name.startswith("."):
                continue
            target = staging / item.name
            if item.is_dir():
                shutil.copytree(item, target)
            elif should_include(item):
                shutil.copy2(item, target)

        if OUT.exists():
            OUT.unlink()

        with ZipFile(OUT, "w", ZIP_DEFLATED) as zf:
            for path in sorted(staging.rglob("*")):
                if should_include(path):
                    zf.write(path, path.relative_to(staging))

    print("wrote", OUT)
    print("zip_size_bytes", OUT.stat().st_size)

if __name__ == "__main__":
    main()
