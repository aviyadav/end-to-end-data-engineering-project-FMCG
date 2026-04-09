import os
import pandas as pd
from src.utils.config import FOLDERS

def run_gold_transformations():
    """Reads Silver data, merges dimensions and facts into a wide table, adds derivations, and saves to Gold."""
    # Read Silver Data
    df_orders = pd.read_parquet(os.path.join(FOLDERS['silver'], 'fact_orders.parquet'))
    df_cust = pd.read_parquet(os.path.join(FOLDERS['silver'], 'dim_customers.parquet'))
    df_prod = pd.read_parquet(os.path.join(FOLDERS['silver'], 'dim_products.parquet'))

    # Merge Tables (Star Schema -> Wide Table)
    df_gold = pd.merge(df_orders, df_cust, on='customer_id', how='left')
    df_gold = pd.merge(df_gold, df_prod, on='product_id', how='left')

    # Data Enrichment (Calculated Column)
    df_gold['revenue'] = df_gold['quantity'] * df_gold['price']

    # Simplification for report and Null management
    df_gold['customer_name'] = df_gold['customer_name'].fillna('Unknown Customer')
    final_cols = ['order_date', 'city', 'category', 'product_name', 'variant', 'revenue', 'quantity']
    df_gold_final = df_gold[final_cols]

    # Save Results
    df_gold_final.to_parquet(os.path.join(FOLDERS['gold'], 'report_master_table.parquet'), index=False)
    df_gold_final.to_csv(os.path.join(FOLDERS['gold'], 'report_master_table.csv'), index=False)

    print("✅ Reporting Table Created in Gold Layer.")
