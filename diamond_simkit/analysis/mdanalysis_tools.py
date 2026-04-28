"""MDAnalysis wrappers."""


def require_mdanalysis() -> None:
    try:
        import MDAnalysis  # noqa: F401
    except ImportError as exc:
        raise ImportError(
            "MDAnalysis is not installed. Install with: pip install MDAnalysis"
        ) from exc


def mdanalysis_placeholder_summary() -> dict:
    require_mdanalysis()
    return {"status": "MDAnalysis available", "note": "add trajectory analyses here"}
