"""Coffee vs Tea — single-letter artifact emitter for the one-letter gate.

The program stores its chosen letter in an output folder, reloads the
bytes from disk, cross-checks them against the expected value, and reports
a compact JSON verdict. Runs on plain Python, no extras required.
"""
import json
import pathlib


def run():
    folder = pathlib.Path("output")
    folder.mkdir(parents=True, exist_ok=True)
    artifact = folder / "entry.txt"
    artifact.write_bytes(LETTER.encode("ascii"))
    raw = artifact.read_bytes().decode("utf-8")
    core = raw.strip()
    if core != LETTER:
        raise ValueError("artifact mismatch: got %r" % core)
    return core


LETTER = "A"  # coffee pick, gate: exactly one character
if __name__ == "__main__":
    result = run()
    print(json.dumps({"result": "ok", "letter": result}))
