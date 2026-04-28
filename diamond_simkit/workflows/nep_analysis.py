"""NEP-analysis placeholders for future calorine-backed workflows."""

from pathlib import Path

from diamond_simkit.analysis.calorine_analysis import require_calorine


def generate_nep_analysis_stub(output_dir: str | Path, potential_path: str) -> Path:
    require_calorine()
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "README.txt").write_text(
        "calorine is available. Add NEP property workflows here.\n"
        f"Potential path: {potential_path}\n"
    )
    return out
