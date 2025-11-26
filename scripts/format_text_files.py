#!/usr/bin/env python3
"""Utility to perform non-destructive formatting of text files in the repository.

It applies the following rules:
 - Normalize line endings to LF
 - Remove trailing whitespace from each line
 - Collapse consecutive empty lines to a single empty line
 - Ensure file finishes with exactly one trailing newline
 - Preserve encoding (attempt UTF-8, fallback to latin-1)

Usage:
    python3 scripts/format_text_files.py [paths ...]
If no paths are provided, script will search the current repo recursively for
files matching *.txt, *.md and *.md.bak
"""
from __future__ import annotations

import sys
from pathlib import Path
import argparse
import re
import io
from typing import List


def read_text_file(path: Path) -> tuple[str, str]:
    """Read a file and return the text and detected encoding.
    Falls back to latin-1 if utf-8 fails."""
    try:
        text = path.read_text(encoding="utf-8")
        return text, "utf-8"
    except UnicodeDecodeError:
        text = path.read_text(encoding="latin-1")
        return text, "latin-1"


def normalize_text(text: str) -> str:
    # Convert CRLF or CR to LF
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # Remove trailing whitespace on each line, but preserve leading indent
    lines = [line.rstrip() for line in text.split('\n')]

    # Collapse consecutive blank lines into a single blank line
    out_lines: List[str] = []
    blank_run = 0
    for l in lines:
        if l == "":
            blank_run += 1
            if blank_run <= 1:
                out_lines.append("")
            # else skip additional blank lines
        else:
            blank_run = 0
            out_lines.append(l)

    # Ensure file ends with a single newline and no trailing spaces
    normalized = "\n".join(out_lines).rstrip() + "\n"
    return normalized


def target_files_from_repo(root: Path) -> List[Path]:
    patterns = ["**/*.txt", "**/*.md", "**/*.md.bak"]
    files: List[Path] = []
    for p in patterns:
        files.extend(list(root.glob(p)))
    # Filter out files in .git or backups folder
    files = [f for f in files if 
             ".git" not in f.parts and "backups" not in f.parts and f.is_file()]
    return sorted(files)


def format_files(files: List[Path]) -> tuple[int, int, int]:
    changed = 0
    skipped = 0
    attempted = 0
    for p in files:
        attempted += 1
        text, enc = read_text_file(p)
        new_text = normalize_text(text)
        if new_text != text:
            p.write_text(new_text, encoding=enc)
            print(f"Formatted: {p}")
            changed += 1
        else:
            skipped += 1
    return attempted, changed, skipped


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Files or directories to process")
    args = parser.parse_args(argv[1:])

    root = Path.cwd()
    if args.paths:
        path_list: List[Path] = []
        for p in args.paths:
            ppath = Path(p)
            if ppath.is_dir():
                path_list.extend(target_files_from_repo(ppath))
            elif ppath.is_file():
                path_list.append(ppath)
            else:
                print(f"Warning: path does not exist: {p}", file=sys.stderr)
        files = path_list
    else:
        files = target_files_from_repo(root)

    if not files:
        print("No files found to format.")
        return 0

    attempted, changed, skipped = format_files(files)
    print(f"Attempted: {attempted}, Changed: {changed}, Skipped: {skipped}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
