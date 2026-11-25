#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut -- make.fun entry.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt: a single line of plain text,
1-200 characters, no setup, no dialogue tags, just the excuse itself.

The line is written in the GPS's own voice: smug, defensive, blaming
the map, with a fresh specific detail (a lake, a bridge, a wedding)
instead of the usual recalculating joke.
"""

import os

LINE = (
    "In my defense, the map swore there was a bridge across that lake, "
    "and the wedding guests only screamed for the first three seconds."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line is %d chars" % len(text)
    assert "\n" not in text, "line must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
