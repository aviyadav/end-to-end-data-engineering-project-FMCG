import os
import pandas as pd
import random
from datetime import datetime, timedelta

from src.utils.config import FOLDERS

def generate_mock_data():
    """Generates dirty/mock customer, product, and order data and saves them as CSV to the Landing zone."""
    landing_path = FOLDERS['landing']

    # --- 1. Customers ---
    customer_ids = range(1001, 1501)
    customers = []
    cities_messy = ['Istanbul', 'Istnbul', 'Ankara', 'Ankr', 'Izmir', None, '  Bursa  ', 'Ankara', 'Izmir', 'Istanbul', 'Ankara', 'Izmir', 'Istanbul']

    for cid in customer_ids:
        name = "Customer " + str(cid)
        if random.random() < 0.3: name = " " + name + " "   # Trim error
        customers.append([cid, name, random.choice(cities_messy), 'TR'])

    df_customers = pd.DataFrame(customers, columns=['customer_id', 'customer_name', 'city', 'market'])
    df_customers.to_csv(os.path.join(landing_path, 'customers.csv'), index=False)
    print("✅ Infrastructure is ready and dirty data has been uploaded to the Landing folder.")

    # --- 2. Products ---
    product_ids = range(1, 201)
    products = []
    product_categories = ['Electronics', 'Home Goods', 'Apparel', 'Books', 'Food', 'confectionery', 'beverages', 'dairy', 'meat', 'seafood', 'bakery', 'frozen foods', 'pantry staples', 'snacks', 'beverages', 'dairy', 'meat', 'seafood', 'bakery', 'frozen foods', 'pantry staples', 'snacks']

    for pid in product_ids:
        name = f"Product {pid}"
        category = random.choice(product_categories)
        price = round(random.uniform(5.0, 500.0), 2)
        products.append([pid, name, category, price])

    df_products = pd.DataFrame(products, columns=['product_id', 'product_name', 'category', 'price'])
    df_products.to_csv(os.path.join(landing_path, 'products.csv'), index=False)
    print("✅ Products data generated and uploaded to Landing folder.")

    # --- 3. Orders ---
    order_ids = range(10001, 15001)
    orders = []

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2025, 12, 31)

    for oid in order_ids:
        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 5)
        order_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        orders.append([oid, customer_id, product_id, quantity, order_date.strftime('%Y-%m-%d')])

    df_orders = pd.DataFrame(orders, columns=['order_id', 'customer_id', 'product_id', 'quantity', 'order_date'])
    df_orders.to_csv(os.path.join(landing_path, 'orders.csv'), index=False)
    print("✅ Orders data generated and uploaded to Landing folder.")
