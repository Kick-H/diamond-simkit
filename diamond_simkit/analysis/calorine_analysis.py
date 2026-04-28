"""calorine wrappers with graceful import errors."""


def require_calorine() -> None:
    try:
        import calorine  # noqa: F401
    except ImportError as exc:
        raise ImportError(
            "calorine is not installed. Install with: pip install calorine"
        ) from exc


def get_calorine_placeholder_summary() -> dict:
    require_calorine()
    return {"status": "calorine available", "note": "implement detailed NEP analyses here"}
