"""Entry for make.fun's "Seventeen Syllables of Debugging" bounty.

Writes one haiku about debugging to entry.txt in the output directory
(three lines, 5-7-5 syllables, 66 UTF-8 characters). The same bytes
are written on every run.
"""

import os

# Draft: "three a.m. cursor / blinks where the red breakpoint waits /
# and the bug was me" — 5-7-5, but "red" is filler added only to reach
# the count, and "the bug was me" is a turn every debugger has heard.
# Revision: drop the adjective, let the breakpoint itself carry the
# line ("a breakpoint that never fires"), and end on the culprit — one
# semicolon. The silence of the log and the unfired breakpoint are
# reframed by a single character.
HAIKU = (
    "cursor blinks at three\n"
    "a breakpoint that never fires\n"
    "one semicolon"
)


def main() -> None:
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    assert all(line.strip() for line in lines), "no line may be blank"
    assert 1 <= len(HAIKU) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    # Read back and confirm the file holds exactly what was intended.
    with open(path, encoding="utf-8") as f:
        assert f.read() == HAIKU, "entry.txt does not match the haiku"


if __name__ == "__main__":
    main()
