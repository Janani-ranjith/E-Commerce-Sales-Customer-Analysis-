# 📊 E-Commerce Sales & Customer Analysis

An interactive web dashboard that turns raw online-store order data into clear business insights: revenue trends, best-selling products, regional and channel performance, and customer segmentation.

Built with **Flask**, **pandas** and **Chart.js**.

---

## 📌 Overview

Online stores generate thousands of orders, but raw data is hard to read. This project analyzes order records automatically and presents the results on a single dashboard, so you can quickly see how the business is performing and who the most valuable customers are.

## ✨ Features

- **KPI cards:** total revenue, orders, customers, average order value, repeat-customer rate
- **Monthly revenue trend:** spot growth, dips and seasonal peaks
- **Category and product analysis:** revenue by category and top-selling products
- **Regional and channel analysis:** sales by region and by Website / Mobile App / Marketplace
- **Customer segmentation:** One-time, Regular (2-3 orders) and Loyal (4+ orders) customers
- **Top customers table:** highest-spending customers with order counts
- **Interactive filters:** filter by region and category; every chart updates instantly
- **Responsive design** with automatic light and dark mode

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Data analysis | pandas, NumPy |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| Data storage | CSV file |

## 📁 Project Structure

```
ecommerce-analysis/
├── app.py              # Flask server and analytics API
├── generate_data.py    # Generates sample order data
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Dashboard page
└── data/
    └── orders.csv      # Created automatically on first run
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or newer
- pip (comes with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS / Linux: `source venv/bin/activate`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```
   On the first run, a sample dataset (`data/orders.csv`, about 6,000 orders) is generated automatically.

5. **Open the dashboard** in your browser at **http://127.0.0.1:5000**

Press `Ctrl + C` in the terminal to stop the server.

## 📂 Using Your Own Data

Replace `data/orders.csv` with your own file and restart the app. The file must contain these columns:

| Column | Description |
|---|---|
| `order_id` | Unique order number |
| `order_date` | Date of the order (YYYY-MM-DD) |
| `customer_id` | Unique customer ID |
| `customer_name` | Customer name |
| `region` | Customer region (e.g. North, South) |
| `channel` | Sales channel (e.g. Website, Mobile App) |
| `category` | Product category |
| `product` | Product name |
| `quantity` | Units purchased |
| `unit_price` | Price per unit |

To regenerate the sample data at any time, delete `data/orders.csv` and run `python generate_data.py`.

## 🔌 API

| Endpoint | Description |
|---|---|
| `GET /` | Dashboard page |
| `GET /api/analytics?region=All&category=All` | JSON with KPIs, trends, segments and top customers |

## 🧯 Troubleshooting

- **`python` not found:** try `python3`, or reinstall Python with "Add to PATH" ticked.
- **Port 5000 already in use:** change `port=5000` at the bottom of `app.py` (for example to `5001`).
- **Charts not showing:** Chart.js loads from a CDN, so an internet connection is required.

## 🔮 Future Improvements

- Date-range filters and year-over-year comparison
- RFM (Recency, Frequency, Monetary) customer scoring
- CSV upload from the browser
- SQLite / PostgreSQL database support
- Sales forecasting with machine learning
- Export reports to PDF or Excel
- User authentication

**Your Name**
GitHub: [@your-username](https://github.com/your-username)
