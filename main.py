#!/usr/bin/env python3
"""Cat Reviews Its Human - make.fun one-line bounty entry.

Reads the entry line from line.txt (next to this file), checks it
against the competition gate (UTF-8 text, a single line, 1-200
characters, not only whitespace), and copies it byte for byte to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

The copy is done at the byte level: the raw bytes are read, decoded
once only to validate the character count and the single-line rule,
then written out unchanged and re-read as bytes to confirm the copy
is identical. Standard library only. No network, no randomness, no
timestamps.
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
        return source.read_bytes(), source
    except FileNotFoundError:
        fail(f"missing source file: {source}")


def check_line(text, raw):
    if not raw:
        fail("line.txt is empty")
    if not text.strip():
        fail("entry is only whitespace")
    if "\n" in text or "\r" in text:
        fail("entry must be a single line")
    if len(text) > MAX_CHARS:
        fail(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")


def main():
    raw, source = read_source()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        fail(f"{SOURCE_NAME} is not valid UTF-8")
    check_line(text, raw)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / TARGET_NAME
    target.write_bytes(raw)
    written = target.read_bytes()
    if written != raw:
        fail(f"wrote {target} but re-reading it gave different bytes")
    print(f"wrote {len(text)} characters to {target}: {text}")


if __name__ == "__main__":
    main()
