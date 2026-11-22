#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is fixed: deterministic, no network, no randomness.
"""

import os

TEXT = (
    "The lighthouse keeper kept one letter he never sent. "
    "On the back, in pencil, a single line \u2014 and the line begins "
    "with your name. "
    "You have read a thousand texts tonight. "
    "None of them told you what it says."
)


def main() -> None:
    # The output directory is created by the program itself.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
