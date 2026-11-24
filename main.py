#!/usr/bin/env python3
"""Cat Reviews Its Human - make.fun one-line bounty entry.

Reads the entry line from line.txt (next to this file), checks it
against the competition gate (UTF-8 text, a single line, 1-200
characters, not only whitespace), and writes it byte for byte to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 200
SOURCE_NAME = "line.txt"
TARGET_NAME = "entry.txt"


def fail(message):
    print(f"main.py: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_source():
    source = Path(__file__).resolve().parent / SOURCE_NAME
    try:
        return source.read_text(encoding="utf-8"), source
    except FileNotFoundError:
        fail(f"missing source file: {source}")
    except UnicodeDecodeError:
        fail(f"{SOURCE_NAME} is not valid UTF-8")


def check_line(text):
    if not text:
        fail("line.txt is empty")
    if not text.strip():
        fail("entry is only whitespace")
    if "\n" in text or "\r" in text:
        fail("entry must be a single line")
    if len(text) > MAX_CHARS:
        fail(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")


def main():
    text, source = read_source()
    check_line(text)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / TARGET_NAME
    target.write_text(text, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != text:
        fail(f"wrote {target} but re-reading it gave different text")
    print(f"wrote {len(text)} characters to {target}")


if __name__ == "__main__":
    main()
