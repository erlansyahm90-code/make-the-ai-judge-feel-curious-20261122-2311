#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

ENTRY = (
    "At 2 a.m. the night librarian finds a book she never shelved, "
    "its pages warm, its margins full of careful notes in her own handwriting. "
    "She turns to the last page. There, in ink not yet dry, is a single line: "
    "'Do not shelve this one yet. It is still being written by you.'"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
