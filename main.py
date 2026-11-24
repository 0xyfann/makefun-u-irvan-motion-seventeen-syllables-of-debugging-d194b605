#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun program/v1 entry.

Writes a single 5-7-5 haiku about debugging to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, no network, no input files, exit 0.
"""

import os

HAIKU = (
    "breakpoint set, I wait\n"
    "the bug walks past in plain sight\n"
    "it waves back at me\n"
)

# Gate (same as the competition's): entry must be 1-200 UTF-8
# characters and not only whitespace. Fail loudly if it ever drifts.
assert 1 <= len(HAIKU) <= 200 and HAIKU.strip()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
