#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (1-2 lines, <=280 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, deterministic, no network.
"""

import os
import sys

ENTRY = (
    "Your father carries you up the stairs at 9:47 p.m., your shoes "
    "dangling from his one finger, your cheek warm against his shoulder. "
    "You mumble something about a dinosaur. He whispers, 'Noted, "
    "captain.' The house holds its breath. Nobody wakes the dinosaur."
)


def main() -> int:
    text = ENTRY
    if not text.strip():
        print("entry is empty or whitespace only", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 280):
        print(f"entry is {len(text)} chars, must be 1-280", file=sys.stderr)
        return 1
    if not (1 <= text.count("\n") + 1 <= 2):
        print("entry must be 1-2 lines", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
