"""Entry program for news-image-20261119.

Copies the front-page image beside this file to the output directory.
Python 3.13, standard library only, no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Deterministic sanity check: the copy must be byte-identical in size
    # and start with the PNG signature, or the run has failed.
    if os.path.getsize(src) != os.path.getsize(dst):
        raise SystemExit("copy size mismatch")
    with open(dst, "rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            raise SystemExit("output is not a PNG")
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
