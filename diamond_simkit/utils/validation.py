"""Small validation helpers."""

from pathlib import Path


def ensure_file_exists(path: str | Path, label: str = "file") -> Path:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"{label} does not exist: {p}")
    return p
