# 🛍️ Customer Segmentation & Predictive Marketing App

This project is a real-world Data Science pipeline for e-commerce businesses. 
It allows users to upload customer data, perform segmentation, and predict campaign response 
with an interactive Streamlit web app.

---

## Project Overview

Businesses often have thousands of customers, but not all behave the same. 
Some shop frequently, some only during sales, some spend a lot, and some rarely shop.  

This app helps analyze customer behavior and make smarter marketing decisions:

1. Customer Segmentation (Clustering)
   - Groups customers based on Recency, Frequency, Monetary (RFM) features.
   - Example segments:
     - High-Value Customers
     - Frequent Buyers
     - Discount-Only Buyers
     - Inactive/At-Risk Customers

2. Predictive Marketing (Classification)
   - Predicts if a customer is likely to respond to a new campaign.
   - Helps businesses target the right customers for promotions.

3. Visual Insights
   - Interactive charts showing customer segments, spending patterns, and behavior trends.

4. Simple Interactive UI
   - Upload CSV/Excel files
   - See segmentation and prediction results immediately
   - No coding required for end users

---

## Features

- RFM feature calculation from e-commerce transactions
- K-Means clustering for customer segmentation
- Random Forest model to predict campaign response
- Interactive Plotly charts
- Streamlit UI for uploading datasets and visualizing results
- Fully deployable online via Streamlit Cloud

---

## Getting Started

### 1. Clone the Repo
git clone https://github.com/<your-username>/customer-segmentation-app.git
cd customer-segmentation-app

### 2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Locally
streamlit run Marketing_App.py

Open the browser at: http://localhost:8501

---

## Dataset Format

Your CSV should include the following columns (example from your e-commerce store):

| Column Name        | Description                   |
|-------------------|-------------------------------|
| Customer No.       | Unique customer identifier    |
| Qty                | Quantity purchased            |
| Sold Price         | Price per item                |
| Purchase Date      | Date of transaction           |
| Job No.            | Unique transaction number     |

Optional Columns: Customer Name, Category, Email, etc.



---

## Technologies Used

- Python 3.13  
- Pandas & NumPy  
- Scikit-learn (KMeans, RandomForest)  
- Plotly (interactive visualization)  
- Streamlit (UI & deployment)

---

## License

This project is open-source for learning and portfolio purposes.
