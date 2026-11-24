"""Two-Sentence Horror entry: writes the story to /output/entry.txt.

Pure stdlib Python. Deterministic: the same bytes on every run.
"""

import os

STORY = (
    "My wife writes our grocery list on the fridge every Sunday, "
    "and I cross things off as I buy them. "
    "This week someone added my name, in her handwriting, "
    "right under the milk."
)


def main():
    # Gate guard: the entry must be 1-400 chars, non-blank, exactly
    # two sentences (two sentence-ending periods, one line).
    text = STORY.strip()
    if not 1 <= len(text) <= 400:
        raise ValueError("story must be 1-400 characters, got %d" % len(text))
    if text.count(".") != 2 or "\n" in text:
        raise ValueError("story must be exactly two sentences on one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")
    print(path)


if __name__ == "__main__":
    main()
