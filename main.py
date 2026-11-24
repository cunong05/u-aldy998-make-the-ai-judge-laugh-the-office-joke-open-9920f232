#!/usr/bin/env python3
"""Write the office-joke entry to /output/entry.txt."""

from pathlib import Path

JOKE = "My calendar finally blocked 'focus time,' so my boss booked a meeting inside it titled 'Quick sync about your focus time.'"


def load_joke():
    """Return the joke from entry.txt next to this file, or JOKE as fallback."""
    try:
        text = (Path(__file__).resolve().parent / "entry.txt").read_text(
            encoding="utf-8"
        ).strip()
    except OSError:
        return JOKE
    return text or JOKE


def main():
    import os

    joke = load_joke()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    print(joke)


if __name__ == "__main__":
    main()
