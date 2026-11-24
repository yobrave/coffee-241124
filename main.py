"""Coffee or Tea one-letter entry.

Emits the single-letter answer into /output/entry.txt, rereads the file,
and verifies the stored byte equals the decision before printing a JSON
verdict. Standard library only, no network, no CLI arguments.
"""
import json
import os

SELECTION = "A"
DISPLAY = {"A": "coffee", "B": "tea"}
KEY = "MAKEFUN_OUTPUT_DIR"


def deliver(target_dir):
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as out:
        out.write(SELECTION)
    with open(path, "r", encoding="utf-8") as back:
        stored = back.read().strip()
    if stored != SELECTION:
        raise RuntimeError("verification failed: stored=%r" % stored)
    return stored


if __name__ == "__main__":
    root = os.environ.get(KEY) or "output"
    final = deliver(root)
    print(json.dumps({"status": "verified", "value": final, "drink": DISPLAY[final]}))
