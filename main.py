#!/usr/bin/env python3
"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Say What Actually Broke" bounty: one line of software error copy (at most 200 characters) that tells the brutal truth about the failure and makes the user laugh.

The program writes exactly that text, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

LINE = "It broke because Dave deployed on a Friday at 4:58 PM and nobody stopped him. Your data is fine; Dave's weekend is not. Error 500, but really: Error Dave."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
