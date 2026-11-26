#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — one funny line from a judgmental till.

The program writes a single line to /output/entry.txt: a remark in the
self-checkout machine's own voice, smug and petty about the shopper's basket,
short enough to fit inside 200 characters.
"""

import os

# Final line: a concrete basket (twelve yoghurts, one lonely carrot) and the
# turn lands in the last words, when even the barcode blushes at the receipt.
LINE = (
    "Twelve yoghurts, no spoon, and one lonely carrot pretending this is a "
    "balanced meal \u2014 I have scanned your choices, weighed your excuses, "
    "and even the barcode blushed when it printed your receipt."
)


def main():
    # The grader mounts the output directory; locally it arrives through
    # MAKEFUN_OUTPUT_DIR, and on the grading image it is /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
