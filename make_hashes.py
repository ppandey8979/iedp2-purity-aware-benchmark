"""Write SHA-256 hashes for every file matching a pattern (sorted).
Usage:  python make_hashes.py "groundtruth_*.txt" HASHES.txt
"""
import glob, hashlib, sys
from pathlib import Path

def sha256(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()

def main(pattern, out):
    files = sorted(glob.glob(pattern))
    lines = [f"{sha256(p)}  {Path(p).name}" for p in files]
    Path(out).write_text("\n".join(lines) + "\n")
    print(f"wrote {len(lines)} hashes to {out}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
