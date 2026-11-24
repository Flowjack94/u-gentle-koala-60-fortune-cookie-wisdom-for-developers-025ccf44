#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes a single original fortune-cookie line for a software developer
to /output/entry.txt. Deterministic: the same line on every run.
"""

FORTUNE = "Your estimate was honest; the deadline heard a promise."

MAX_CHARS = 120


def main() -> None:
    text = FORTUNE

    # Gate checks, mirroring the competition gate: UTF-8 text,
    # 1-120 characters, not only whitespace, a single line.
    encoded = text.encode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"fortune is {len(text)} chars, must be 1-120")
    if not text.strip():
        raise SystemExit("fortune must not be only whitespace")
    if text != text.strip():
        raise SystemExit("fortune must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("fortune must be a single line")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
