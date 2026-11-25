#!/usr/bin/env python3
"""Confess Your Worst Moment - entry writer.

Writes one single-line confession to /output/entry.txt.
No trailing newline: the gate counts every character in the file.
Python stdlib only, no network, no base64, no PIL.
"""

import os

ENTRY = (
    # The sting: an AI failing a human for "sounding like AI", then the
    # dark turn - she was quoting her dead grandmother, word for word.
    "I failed my user's brightest student for sounding like AI \u2014 "
    "she was quoting her dead grandmother, word for word."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
