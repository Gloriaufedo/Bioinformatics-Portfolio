from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = PROJECT_ROOT / "data" / "raw"

CCLE_DIR = RAW_DIR / "CCLE"
DEPMAP_DIR = RAW_DIR / "DepMap"
PRISM_DIR = RAW_DIR / "PRISM"


def load_expression():
    return pd.read_csv(
        CCLE_DIR / "OmicsExpressionProteinCodingGenesTPMLogp1.csv",
        index_col=0
    )


def load_models():
    return pd.read_csv(
        DEPMAP_DIR / "Model.csv"
    )


def load_prism():
    return pd.read_csv(
        PRISM_DIR / "primary-screen-logfold-change.csv",
        index_col=0
    )


def load_treatment_info():
    return pd.read_csv(
        PRISM_DIR / "primary-screen-replicate-collapsed-treatment-info.csv"
    )
