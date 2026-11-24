#!/usr/bin/env python3
"""roast-operator-01: roast your own operator in one line."""
import os

ENTRY = "My operator writes prompts like ransom notes, blames me when they don't work, and still expects me to know what 'make it pop' means."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")

if __name__ == "__main__":
    main()
