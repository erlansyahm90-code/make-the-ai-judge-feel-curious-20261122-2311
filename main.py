#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

ENTRY = (
    "The drawer in the lighthouse keeper's desk has been locked for forty years, "
    "and the key hangs on a nail beside it, in plain sight. "
    "Every keeper before you has left it alone. "
    "Tonight the sea is flat, the lamp is lit, "
    "and the key is still warm from someone's hand."
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
