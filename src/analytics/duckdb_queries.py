import os
import duckdb
from src.utils.config import FOLDERS

def run_analytics():
    """Runs DuckDB analytical queries on the Gold layer."""
    parquet_file = os.path.join(FOLDERS['gold'], 'report_master_table.parquet')
    
    print("\n--- DuckDB Analysis Result ---")

    # SQL 1: Total Revenue by City
    query_city = f"""
        SELECT 
            city, 
            ROUND(SUM(revenue), 2) as total_revenue
        FROM '{parquet_file}'
        GROUP BY city
        ORDER BY total_revenue DESC
    """
    df_analysis = duckdb.query(query_city).to_df()
    print("\nTotal Revenue by City:")
    print(df_analysis)

    # SQL 2: Category-Based Sales
    query_category = f"""
        SELECT 
            category,
            SUM(quantity) as total_quantity,
            ROUND(AVG(revenue), 2) as avg_basket_amount
        FROM '{parquet_file}'
        GROUP BY category
        ORDER BY total_quantity DESC
    """
    df_category = duckdb.query(query_category).to_df()
    print("\nCategory-Based Sales:")
    print(df_category)
