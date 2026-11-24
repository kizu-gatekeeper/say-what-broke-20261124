#!/usr/bin/env python3
"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Say What Actually Broke" bounty: one line of software error copy (at most 200 characters) that tells the brutal truth about the failure and makes the user laugh.

The program writes exactly that text, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

LINE = "It broke because Dave deployed on a Friday at 4:58 PM and nobody stopped him. Your data is fine; Dave's weekend is not. Error 500, but really: Error Dave."


def write_entry(out_dir: str) -> str:
    """Write the entry text to ``entry.txt`` in ``out_dir``; return its path.

    The file holds exactly the entry and nothing else: no trailing
    newline, no extra whitespace, so the gate reads the text alone.
    """
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return entry_path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
