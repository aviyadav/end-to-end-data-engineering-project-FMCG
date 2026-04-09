import os
import pandas as pd
from datetime import datetime
from src.utils.config import FOLDERS

def ingest_to_bronze(file_name, source_folder, target_folder):
    """Moves data from Landing (CSV) to Bronze layer (Parquet) and appends audit columns."""
    source_path = os.path.join(source_folder, f"{file_name}.csv")
    target_path = os.path.join(target_folder, f"{file_name}.parquet")

    try:
        # Read CSV
        df = pd.read_csv(source_path)

        # Add Audit Columns
        df['_ingestion_timestamp'] = datetime.now()
        df['_source_file'] = f"{file_name}.csv"

        # Save as Parquet
        df.to_parquet(target_path, index=False)
        print(f"✅ {file_name} -> Moved to Bronze layer.")

    except Exception as e:
        print(f"❌ Error: {e}")

def run_bronze_ingestion():
    files = ['customers', 'products', 'orders']
    for f in files:
        ingest_to_bronze(f, FOLDERS['landing'], FOLDERS['bronze'])
