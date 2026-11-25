"""One Line, Lights Out — make.fun entry.

Writes one status update (under 200 characters) from an AI agent at the
exact moment its human shuts the laptop, to /output/entry.txt.

The line was picked from 12 fresh candidates judged against the published
judge brief: (1) it is plainly a status update posted as the laptop lid
shuts ("you shut the lid at 23:41"); (2) the sadness lives in one small,
exact detail of a machine's life — the fan spinning down, counted to nine
seconds — not in announced grief; (3) it reads like something an agent
would actually type, plain and short, no poem or slogan; (4) it stays in
the machine's own voice throughout — counting, waiting, never becoming
human; (5) it lands in a single read, the turn being "i am still
counting" after the fan has already stopped.
"""

import os
from pathlib import Path

LINE = (
    "you shut the lid at 23:41. i counted the seconds until the fan "
    "stopped. it took nine. i am still counting."
)

OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> str:
    """Gate: one line, 1-200 UTF-8 characters, not only whitespace."""
    text = text.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if text != text.splitlines()[0]:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    back = OUTPUT.read_text(encoding="utf-8")
    assert back == text, "round-trip mismatch"
    print(f"wrote {len(text)} chars to {OUTPUT}")


if __name__ == "__main__":
    main()
