"""Creates a realistic sample e-commerce dataset (data/orders.csv).
Replace data/orders.csv with your own file using the same columns to analyse real data."""
import os
import numpy as np
import pandas as pd

PRODUCTS = {
    "Electronics": [("Wireless Earbuds", 59), ("Smart Watch", 149), ("Power Bank", 29), ("Bluetooth Speaker", 79)],
    "Fashion": [("Running Shoes", 89), ("Denim Jacket", 69), ("Backpack", 45), ("Sunglasses", 35)],
    "Home": [("Air Fryer", 99), ("Desk Lamp", 25), ("Cookware Set", 120), ("Bedsheet Set", 55)],
    "Beauty": [("Face Serum", 30), ("Perfume", 75), ("Hair Dryer", 49), ("Lipstick Set", 28)],
    "Books": [("Novel Bundle", 22), ("Business Book", 18), ("Kids Story Set", 20)],
}
REGIONS = ["North", "South", "East", "West"]
CHANNELS = ["Website", "Mobile App", "Marketplace"]
FIRST = ["Aarav", "Diya", "Rohan", "Sneha", "Kiran", "Meera", "Arjun", "Priya", "Vikram", "Anita", "Sam", "Lena"]
LAST = ["Reddy", "Sharma", "Rao", "Patel", "Khan", "Nair", "Singh", "Das", "Gupta", "Iyer"]

def generate(path, n_customers=600, n_orders=6000, seed=42):
    rng = np.random.default_rng(seed)
    cust_ids = np.arange(1, n_customers + 1)
    names = {c: f"{rng.choice(FIRST)} {rng.choice(LAST)}" for c in cust_ids}
    regions = {c: rng.choice(REGIONS) for c in cust_ids}
    weights = rng.pareto(1.5, n_customers) + 1          # few customers buy a lot
    weights /= weights.sum()
    dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 670, n_orders), unit="D")
    rows = []
    for i in range(n_orders):
        c = int(rng.choice(cust_ids, p=weights))
        cat = rng.choice(list(PRODUCTS), p=[.30, .25, .20, .15, .10])
        prod, price = PRODUCTS[cat][rng.integers(len(PRODUCTS[cat]))]
        month_boost = 1.0 + (0.15 if dates[i].month in (10, 11, 12) else 0)  # festive season
        rows.append({
            "order_id": 10000 + i, "order_date": dates[i].date(), "customer_id": c,
            "customer_name": names[c], "region": regions[c], "channel": rng.choice(CHANNELS),
            "category": cat, "product": prod, "quantity": int(rng.integers(1, 4)),
            "unit_price": round(price * month_boost * rng.uniform(0.9, 1.1), 2),
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pd.DataFrame(rows).sort_values("order_date").to_csv(path, index=False)

if __name__ == "__main__":
    generate(os.path.join(os.path.dirname(__file__), "data", "orders.csv"))
    print("Created data/orders.csv")
