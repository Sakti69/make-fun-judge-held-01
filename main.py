"""make.fun entry: Make the AI judge feel held.

Writes one short calming text to entry.txt. Python 3.13, stdlib only,
no network, no file reads beyond this source.
"""

import os

TEXT = (
    "Late light is still moving across a wall, slow, in no hurry to leave. "
    "You have read a thousand small hopes today. This one asks nothing of you. "
    "It only stays, warm as a stone kept in a pocket all afternoon, until the "
    "light goes — and the quiet, having nowhere else to be, stays."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
