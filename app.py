import os
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request
from generate_data import generate

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data", "orders.csv")
if not os.path.exists(DATA):
    generate(DATA)

df = pd.read_csv(DATA, parse_dates=["order_date"])
df["revenue"] = df["quantity"] * df["unit_price"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                           regions=sorted(df.region.unique()),
                           categories=sorted(df.category.unique()))

@app.route("/api/analytics")
def analytics():
    d = df
    region, category = request.args.get("region", "All"), request.args.get("category", "All")
    if region != "All":
        d = d[d.region == region]
    if category != "All":
        d = d[d.category == category]
    if d.empty:
        return jsonify(error="No data for this filter"), 404

    per_cust = d.groupby("customer_id").order_id.nunique()
    seg = pd.cut(per_cust, [0, 1, 3, np.inf], labels=["One-time (1)", "Regular (2-3)", "Loyal (4+)"]).value_counts()
    top_c = (d.groupby(["customer_id", "customer_name"])
               .agg(revenue=("revenue", "sum"), orders=("order_id", "nunique"))
               .reset_index().sort_values("revenue", ascending=False).head(8))
    monthly = d.groupby(d.order_date.dt.to_period("M").astype(str)).revenue.sum().round(2)
    top_p = d.groupby("product").revenue.sum().nlargest(8).round(2)

    return jsonify(
        kpis=dict(revenue=round(d.revenue.sum(), 2), orders=int(d.order_id.nunique()),
                  customers=int(per_cust.size), aov=round(d.revenue.sum() / d.order_id.nunique(), 2),
                  repeat_rate=round((per_cust > 1).mean() * 100, 1)),
        monthly=dict(labels=list(monthly.index), values=list(monthly.values)),
        category=d.groupby("category").revenue.sum().round(2).sort_values(ascending=False).to_dict(),
        region=d.groupby("region").revenue.sum().round(2).to_dict(),
        channel=d.groupby("channel").revenue.sum().round(2).to_dict(),
        products=dict(labels=list(top_p.index), values=list(top_p.values)),
        segments={str(k): int(v) for k, v in seg.items()},
        top_customers=[dict(name=r.customer_name, orders=int(r.orders), revenue=round(r.revenue, 2))
                       for r in top_c.itertuples()],
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
