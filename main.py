#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
``<output_dir>/entry.txt``.

The output directory is taken from the ``OUTPUT_DIR`` environment
variable, then ``MAKEFUN_OUTPUT_DIR``, then the default ``/output``.

The entry is validated before writing: it must be UTF-8 text of
1 to 400 characters and not only whitespace.
"""

import os
import sys

ENTRY = (
    "Our router needs restarting every 47 minutes, and nobody in this house "
    "knows why, including the man we paid $90 to look at it. He stared at "
    "the blinking light, said 'huh,' and left. The light is still blinking. "
    "It blinks in Morse code for help and I am starting to understand it."
)


def output_dir() -> str:
    return (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("error: entry is empty or whitespace only", file=sys.stderr)
        return 1
    if len(text) > 400:
        print(f"error: entry is {len(text)} characters, over the 400 cap",
              file=sys.stderr)
        return 1
    # No stray control characters (other than ordinary whitespace) may
    # sneak into the entry text.
    if any(ord(ch) < 32 and ch not in "\t\n\r" for ch in text):
        print("error: entry contains control characters", file=sys.stderr)
        return 1
    # Must round-trip as UTF-8.
    text.encode("utf-8")

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
