import os
import pandas as pd
import hashlib
import re
from src.utils.config import FOLDERS

def clean_customers():
    df_cust = pd.read_parquet(os.path.join(FOLDERS['bronze'], 'customers.parquet'))
    df_cust['customer_name'] = df_cust['customer_name'].str.strip()
    city_map = {'Istnbul': 'Istanbul', 'Ankr': 'Ankara', '  Bursa  ': 'Bursa'}
    df_cust['city'] = df_cust['city'].replace(city_map).fillna('Unknown').str.strip()
    df_cust.to_parquet(os.path.join(FOLDERS['silver'], 'dim_customers.parquet'), index=False)

def extract_variant(text):
    match = re.search(r'(\d+(?:g|kg|ml|tabs))', text, re.IGNORECASE)
    return match.group(0) if match else 'Regular'

def clean_products():
    df_prod = pd.read_parquet(os.path.join(FOLDERS['bronze'], 'products.parquet'))
    df_prod['variant'] = df_prod['product_name'].apply(extract_variant)
    df_prod['product_code'] = df_prod['product_name'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest()[:16])
    df_prod.to_parquet(os.path.join(FOLDERS['silver'], 'dim_products.parquet'), index=False)

def clean_orders():
    df_ord = pd.read_parquet(os.path.join(FOLDERS['bronze'], 'orders.parquet'))
    df_ord['order_date'] = pd.to_datetime(df_ord['order_date'], format='mixed', errors='coerce')
    df_ord = df_ord.dropna(subset=['order_date'])
    df_ord.to_parquet(os.path.join(FOLDERS['silver'], 'fact_orders.parquet'), index=False)

def run_silver_transformations():
    clean_customers()
    clean_products()
    clean_orders()
    print("🚀 Silver Layer (Clean Data) Ready!")
