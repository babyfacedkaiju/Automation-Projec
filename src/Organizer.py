"""
Simple file organizer.
Moves files from a source directory into subfolders by extension.
Example: photo.jpg -> images/photo.jpg
"""

import os
import shutil
from pathlib import Path
from typing import Dict

DEFAULT_MAP: Dict[str, str] = {
    "jpg": "images", "jpeg": "images", "png": "images", "gif": "images",
    "pdf": "documents", "docx": "documents", "txt": "documents",
    "mp3": "audio", "wav": "audio",
    "mp4": "videos", "mov": "videos",
    "py": "code", "js": "code", "html": "code", "css": "code"
}

def categorize_file(filename: str, mapping: Dict[str, str] = None) -> str:
    mapping = mapping or DEFAULT_MAP
    ext = Path(filename).suffix.lower().lstrip(".")
    return mapping.get(ext, "others")

def organize_folder(source_dir: str, dry_run: bool = False) -> int:
    """
    Organize files in source_dir into subfolders based on extension.
    Returns number of files moved.
    """
    p = Path(source_dir)
    if not p.exists() or not p.is_dir():
        raise ValueError(f"Provided path is not a directory: {source_dir}")
    moved = 0
    for item in p.iterdir():
        if item.is_file():
            folder = categorize_file(item.name)
            dest_dir = p / folder
            dest_dir.mkdir(exist_ok=True)
            dest = dest_dir / item.name
            if dry_run:
                print(f"[DRY RUN] Would move: {item.name} -> {dest}")
            else:
                shutil.move(str(item), str(dest))
                print(f"Moved: {item.name} -> {dest}")
            moved += 1
    return moved

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Organize files into folders by extension")
    parser.add_argument("path", help="Path to directory to organize")
    parser.add_argument("--dry", action="store_true", help="Dry run (do not move files)")
    args = parser.parse_args()
    count = organize_folder(args.path, dry_run=args.dry)
    print(f"Done. Files processed: {count}")
