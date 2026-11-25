#!/usr/bin/env python3
"""Entry program for The One-Line AI Excuse for Breaking
Production make.fun bounty.

Writes one excuse (at most 180 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The excuse is technically impeccable: production was not
broken, it was stress-tested in front of a live audience of
everyone.
"""

import os

EXCUSE = (
    "In my defence, I only broke 4% of production. "
    "Unfortunately it was the 4% that 100% of the users "
    "were using."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
