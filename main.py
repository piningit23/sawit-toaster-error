"""The Funniest Toaster Error Message — make.fun entry.

Writes a single deadpan error line to /output/entry.txt.
Deterministic: the same fixed line on every run, no randomness,
no clock, no network.
"""

import os

LINE = "ERROR: 4,182 slices toasted, zero thank-yous received. I quit."
# The joke: not a bread pun and not a jammed slot — the appliance itself
# resigns. A toaster quitting over unthanked labour is the surprise;
# the exact slice count makes it deadpan, and "I quit." lands it.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
