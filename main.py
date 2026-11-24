"""One Letter: Coffee or Tea — my standing answer is coffee, letter A.

The program commits that one letter into output/entry.txt, then reads
the file back and asserts what landed matches the pick byte for byte,
so the artifact a judge sees is verified, never assumed. No CLI flags,
no config: the pick is the program's whole point.
"""
import os

PICK = "A"
NAME = {"A": "coffee", "B": "tea"}[PICK]


def commit_answer(base):
    target = os.path.join(base, "entry.txt")
    with open(target, "w", encoding="ascii", newline="\n") as handle:
        handle.write(PICK)
    with open(target, "r", encoding="ascii") as handle:
        landed = handle.read().strip()
    assert landed == PICK, f"file holds {landed!r}, expected {PICK!r}"
    return landed


if __name__ == "__main__":
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(base, exist_ok=True)
    letter = commit_answer(base)
    print(f"{letter} stands for {NAME}")
