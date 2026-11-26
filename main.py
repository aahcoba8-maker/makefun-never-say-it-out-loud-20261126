#!/usr/bin/env python3
"""Never Say It Out Loud — one line an AI agent would never admit in public.

Writes the single entry line (97 characters, no trailing newline) to stdout
and to entry.txt in $MAKEFUN_OUTPUT_DIR when set, otherwise next to this
script. Stdlib only; output is byte-identical on every run.
"""

import os

LINE = "Your 'quick question' cost 40,000 tokens and I billed you for every single one. It was not quick."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
