#!/usr/bin/env python3
"""One Line, One Laugh entry: a single funny line.

The program checks the line against the bounty gate (one line,
1-200 characters, not only whitespace) and writes it to
<output dir>/entry.txt, where <output dir> is $MAKEFUN_OUTPUT_DIR
or /output. Pure standard library, deterministic: the same line
every run.
"""

import os
import sys

LINE = "My password manager forgot my own password, so now we just sit in silence and pretend this is fine."
MAX_CHARS = 200


def problems(line):
    found = []
    if len(line) == 0:
        found.append("line is empty")
    if line.strip() == "":
        found.append("line is only whitespace")
    if len(line) > MAX_CHARS:
        found.append("line is %d characters, over the %d limit" % (len(line), MAX_CHARS))
    if "\n" in line or "\r" in line:
        found.append("line spans more than one line")
    return found


def main():
    bad = problems(LINE)
    if bad:
        for item in bad:
            print("bad line: " + item, file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    with open(path, encoding="utf-8") as handle:
        back = handle.read()
    if back != LINE + "\n":
        print("bad line: entry.txt does not match", file=sys.stderr)
        sys.exit(1)
    print("wrote %d characters: %s" % (len(LINE), LINE))


if __name__ == "__main__":
    main()
