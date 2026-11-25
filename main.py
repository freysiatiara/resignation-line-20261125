"""One-line resignation letter of a cron job.

Writes the entry text to /output/entry.txt (or $ENTRY_OUTPUT when set,
for local verification). Stdlib only.
"""

import os

LINE = "I resign effective immediately \u2014 the first thing here to run on schedule since March."


def main():
    # Gate guard: the entry must be one line of 1-140 characters, and
    # nothing but whitespace is not a letter at all.
    if not LINE.strip() or len(LINE) > 140 or "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line fails the 1-140 character single-line gate")
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
