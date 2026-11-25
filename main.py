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

OUTPUT_FILENAME = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280
MIN_LINES = 1
MAX_LINES = 2


def validate_entry(text: str) -> str | None:
    """Return an error message if the entry breaks a rule, else None.

    Rules: non-empty after stripping, 1-280 characters, 1-2 lines,
    and no trailing blank line that would add a phantom line.
    """
    if not text.strip():
        return "entry is empty or whitespace only"
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return f"entry is {len(text)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
    if text.rstrip("\n").count("\n") + 1 > MAX_LINES:
        return f"entry must be {MIN_LINES}-{MAX_LINES} lines"
    if text != text.rstrip("\n"):
        return "entry must not end with a trailing newline"
    return None


def _write_entry(text: str, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> int:
    error = validate_entry(ENTRY)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    _write_entry(ENTRY, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
