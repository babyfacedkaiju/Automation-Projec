import tempfile
import os
from pathlib import Path
from src.organizer import organize_folder

def test_organize_folder_creates_folders(tmp_path):
    # Create sample files
    (tmp_path / "a.jpg").write_text("dummy")
    (tmp_path / "b.txt").write_text("dummy")
    moved = organize_folder(str(tmp_path), dry_run=False)
    # Check folders
    assert (tmp_path / "images" / "a.jpg").exists()
    assert (tmp_path / "documents" / "b.txt").exists()
    assert moved == 2
