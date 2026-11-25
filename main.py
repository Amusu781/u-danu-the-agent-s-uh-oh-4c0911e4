#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word: googling. The agent doesn't know, so it quietly googles the
answer mid-task — the machine equivalent of flipping through the textbook
during the exam.
"""

import os

WORD = "googling"
OUTPUT_PATH = "/output/entry.txt"


def write_entry(path: str, word: str) -> None:
    """Write the word with no trailing newline; never removes the directory."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    with open(path, "rb") as f:
        assert f.read() == word.encode("utf-8"), "output must be exactly the word"


def main() -> None:
    assert 1 <= len(WORD) <= 99
    assert not any(c.isspace() for c in WORD)
    write_entry(OUTPUT_PATH, WORD)


if __name__ == "__main__":
    main()
