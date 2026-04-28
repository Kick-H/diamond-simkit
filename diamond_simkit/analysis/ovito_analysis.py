"""OVITO/ovitos integration helpers."""

import shutil


def require_ovito_python() -> None:
    try:
        import ovito  # noqa: F401
    except ImportError as exc:
        raise ImportError(
            "OVITO Python module is not installed. Install with: pip install ovito"
        ) from exc


def find_ovitos_executable() -> str:
    exe = shutil.which("ovitos")
    if exe is None:
        raise RuntimeError("ovitos executable not found in PATH")
    return exe
