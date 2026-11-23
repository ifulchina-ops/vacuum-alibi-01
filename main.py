#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters.

A robot vacuum's deadpan excuse for missing a spot, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).
"""

import os

LINE = "I did not miss that spot. My lidar classified the crumbs as a protected habitat, and I am forbidden from disturbing wildlife."


def main():
    # Enforce the bounty gate before writing: one line, 1-200 characters,
    # and more than whitespace — the sealed scorer refuses anything else.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
