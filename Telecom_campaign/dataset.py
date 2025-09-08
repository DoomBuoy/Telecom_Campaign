from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from Telecom_campaign.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()
import os
os.system('poetry update')
os.system('poetry install')
os.system('poetry lock')

# Get the absolute path to the project root
project_root = Path(__file__).resolve().parent.parent
processed_dir = project_root / 'data' / 'processed'
processed_dir.mkdir(parents=True, exist_ok=True)
@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    import subprocess

    logger.info("Starting download of Telecom dataset to raw folder...")
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_name = "TeleCom_Data.csv"
    file_id = "16zmOEpthbUJsq3SYojJGVAenRIHcRdUl"
    dest_path = RAW_DATA_DIR / file_name
    url = f"https://drive.google.com/uc?id={file_id}"

    try:
        import gdown
    except ImportError:
        logger.info("gdown not found, installing...")
        subprocess.check_call(["pip", "install", "gdown"])
        import gdown

    logger.info(f"Downloading {file_name} from Google Drive...")
    try:
        gdown.download(url, str(dest_path), quiet=False)
        logger.success(f"Downloaded {file_name} to {dest_path}")
    except Exception as e:
        logger.error(f"Failed to download {file_name}: {e}")

    logger.success("File downloaded to raw folder.")


if __name__ == "__main__":
    app()
