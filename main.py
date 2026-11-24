#!/usr/bin/env python3
"""Write the office-joke entry to /output/entry.txt."""

JOKE = "My calendar finally blocked 'focus time,' so my boss booked a meeting inside it titled 'Quick sync about your focus time.'"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
