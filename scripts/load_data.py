import pandas as pd
from sqlalchemy import create_engine
import os

# Paths
DATA_DIR = "data"
DB_PATH = "outputs/olist.db"

# Map CSV filenames to the table names we want in the database
csv_to_table = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "order_payments",
    "olist_order_reviews_dataset.csv": "order_reviews",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "olist_geolocation_dataset.csv": "geolocation",
    "product_category_name_translation.csv": "product_category_translation",
}

def main():
    os.makedirs("outputs", exist_ok=True)
    engine = create_engine(f"sqlite:///{DB_PATH}")

    for csv_file, table_name in csv_to_table.items():
        path = os.path.join(DATA_DIR, csv_file)
        print(f"Loading {csv_file} into table '{table_name}'...")
        df = pd.read_csv(path)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"  -> {len(df)} rows loaded.")

    print("\nAll tables loaded successfully into", DB_PATH)

if __name__ == "__main__":
    main()