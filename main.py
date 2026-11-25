"""Write the entry sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.

One sentence, at most 200 characters, about the best advice I ever got.
Validated before writing: non-empty, <= 200 chars, single line, ASCII,
exactly one sentence (one terminal period).
"""

import os
import sys

SENTENCE = (
    "The night my shop burned down, my uncle put a hand on my shoulder "
    "and said rebuild it smaller, because a business you can carry in "
    "one trip is one nobody can take from you."
)


def validate(text: str) -> None:
    if not text or text.strip() == "":
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        raise ValueError("entry must be ASCII only")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in one period")


def main() -> None:
    validate(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="ascii") as f:
        f.write(SENTENCE)
    print(f"wrote {len(SENTENCE)} chars to {path}")


if __name__ == "__main__":
    main()
