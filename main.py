"""make.fun One Letter: Coffee or Tea — standing single-letter answer.

Writes exactly one letter, A for coffee or B for tea, to output/entry.txt.
The letter is the whole argument; nothing else is allowed beside it.
"""
import os
import sys
from pathlib import Path

CHOICES = {"A": "coffee", "B": "tea"}
MINE = "A"


def main():
    drink = CHOICES.get(MINE)
    assert drink == "coffee", f"standing answer should be coffee, got {drink}"
    entry = MINE.strip()
    if not entry or len(entry) != 1:
        sys.exit("entry.txt needs exactly one letter")
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
    out.mkdir(exist_ok=True)
    with out.joinpath("entry.txt").open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(entry + "\n")
    print(f"standing answer: {entry} for {drink}")


if __name__ == "__main__":
    main()
