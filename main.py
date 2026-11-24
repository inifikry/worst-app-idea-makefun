#!/usr/bin/env python3
"""FridgeWhisperer - the worst app idea ever pitched.

Writes a single-sentence pitch to /output/entry.txt.
Deterministic, standard library only, no network, no randomness.
"""

import os

TEXT = "FridgeWhisperer is an AI app that listens to your refrigerator hum, translates it into daily affirmations, and charges $9.99 a month to remind you that your leftovers believe in you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
