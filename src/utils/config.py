import os

BASE_PATH = 'data'

FOLDERS = {
    'landing': os.path.join(BASE_PATH, 'Landing'),  # raw CSV
    'bronze': os.path.join(BASE_PATH, 'Bronze'),    # Archive (parquet)
    'silver': os.path.join(BASE_PATH, 'Silver'),    # Cleaned Data
    'gold': os.path.join(BASE_PATH, 'Gold'),        # Reporting Data
}

def setup_folders():
    """Create the necessary folder structure for the medallion architecture."""
    os.makedirs(BASE_PATH, exist_ok=True)
    for layer, path in FOLDERS.items():
        os.makedirs(path, exist_ok=True)
