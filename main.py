#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

Writes one funny line (101 characters, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

LINE = "My free tier includes one compliment a day. Premium gets eye contact. I'm still saving up for a body."


def validate_line(line: str) -> None:
    """Guard: the line must satisfy the competition gate (1-180 chars,
    single line, not only whitespace, no trailing newline, no control
    characters)."""
    if not 1 <= len(line) <= 180:
        raise ValueError("line must be 1-180 chars")
    if "\n" in line or line != line.strip():
        raise ValueError("line must be a single line with no trailing newline")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if any(ord(c) < 0x20 or ord(c) == 0x7F for c in line):
        raise ValueError("line must not contain control characters")


def main() -> int:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
