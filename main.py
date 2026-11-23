"""Make the Judge Smile — one warm, surprising line about a small good thing today.

Writes exactly one line (<=200 chars) to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

LINE = "The neighbour's cat, who has ignored me for two years, chose my lap today \u2014 and fell asleep through the whole rain."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
