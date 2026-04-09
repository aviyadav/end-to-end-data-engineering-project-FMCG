from src.utils.config import setup_folders
from src.pipeline.generate_data import generate_mock_data
from src.pipeline.bronze import run_bronze_ingestion
from src.pipeline.silver import run_silver_transformations
from src.pipeline.gold import run_gold_transformations
from src.analytics.duckdb_queries import run_analytics

def main():
    print("=== FMCG Data Engineering Pipeline ===")
    
    print("\n[1/6] Setting up Folder Structure...")
    setup_folders()

    print("\n[2/6] Generating Raw/Mock Data (Landing)...")
    generate_mock_data()

    print("\n[3/6] Ingesting to Bronze Layer (Parquet + Auditing)...")
    run_bronze_ingestion()

    print("\n[4/6] Transforming to Silver Layer (Cleaning & Standardizing)...")
    run_silver_transformations()

    print("\n[5/6] Building Gold Layer (Reporting Wide Table)...")
    run_gold_transformations()

    print("\n[6/6] Running Analytics (DuckDB)...")
    run_analytics()

    print("\n=== Pipeline Execution formatting complete ===")

if __name__ == '__main__':
    main()