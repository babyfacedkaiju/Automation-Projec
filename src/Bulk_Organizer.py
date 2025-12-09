"""
Bulk rename files in a directory by adding a prefix or suffix.
"""

from pathlib import Path
from typing import Optional

def bulk_rename(directory: str, prefix: Optional[str]=None, suffix: Optional[str]=None) -> int:
    p = Path(directory)
    if not p.exists() or not p.is_dir():
        raise ValueError("Directory does not exist.")
    count = 0
    for f in p.iterdir():
        if f.is_file():
            name = f.stem
            ext = f.suffix
            new_name = f"{prefix or ''}{name}{suffix or ''}{ext}"
            f.rename(p / new_name)
            count += 1
    return count

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--prefix", default="")
    parser.add_argument("--suffix", default="")
    args = parser.parse_args()
    n = bulk_rename(args.path, prefix=args.prefix, suffix=args.suffix)
    print(f"Renamed {n} files.")
