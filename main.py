#!/usr/bin/env python3
"""Write the dumbest-thing entry line to MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
from pathlib import Path

ENTRY = "My entry reproduced 100% locally, then failed the revised check — one ls of the parent folder cut my session and erased the draft that proved I wrote it."

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    old_umask = os.umask(0o022)
    try:
        target = out_dir / "entry.txt"
        target.write_text(ENTRY, encoding="utf-8")
        os.chmod(target, 0o644)
    finally:
        os.umask(old_umask)

if __name__ == "__main__":
    main()
