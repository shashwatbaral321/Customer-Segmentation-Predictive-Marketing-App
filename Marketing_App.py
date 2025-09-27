import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ---------------------------
# TITLE
# ---------------------------
st.title("🛍️ Customer Segmentation & Predictive Marketing App")

st.markdown("""
This app allows you to:
1. Upload customer data (CSV/Excel)
2. Perform segmentation (Clustering)
3. Predict campaign response
""")

# ---------------------------
# FILE UPLOAD
# ---------------------------
uploaded_file = st.file_uploader("Upload your customer dataset", type=["csv", "xlsx"])

if uploaded_file:
    # Load data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### 📊 Preview of Data")
    st.dataframe(df.head())

    # ---------------------------
    # RFM FEATURE ENGINEERING
    # ---------------------------
    required_cols = ['Customer No.', 'Qty', 'Sold Price', 'Purchase Date', 'Job No.']
    if all(col in df.columns for col in required_cols):
        # Compute Total Sales
        df['TotalSum'] = df['Qty'] * df['Sold Price']

        # Convert Purchase Date to datetime
        df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], errors='coerce')

        # RFM calculation
        rfm = df.groupby('Customer No.').agg({
            'Purchase Date': lambda x: (df['Purchase Date'].max() - x.max()).days,
            'Job No.': 'count',
            'TotalSum': 'sum'
        }).reset_index()

        # Rename columns for RFM
        rfm.rename(columns={'Purchase Date':'Recency', 'Job No.':'Frequency', 'TotalSum':'Monetary', 'Customer No.':'CustomerID'}, inplace=True)

        st.write("### 🔍 RFM Features")
        st.dataframe(rfm.head())

        # ---------------------------
        # CUSTOMER SEGMENTATION
        # ---------------------------
        st.write("## 📌 Customer Segmentation (Clustering)")
        scaler = StandardScaler()
        rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

        kmeans = KMeans(n_clusters=4, random_state=42)
        rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

        fig = px.scatter(rfm, x="Recency", y="Monetary",
                         size="Frequency", color="Cluster",
                         hover_data=['CustomerID'])
        st.plotly_chart(fig)

        # ---------------------------
        # PREDICTIVE MODEL
        # ---------------------------
        st.write("## 🎯 Predict Campaign Response")
        # Fake target for demo (replace with real campaign response data)
        rfm['Response'] = np.random.randint(0, 2, size=len(rfm))

        X = rfm[['Recency', 'Frequency', 'Monetary']]
        y = rfm['Response']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train, y_train)

        preds = clf.predict(X_test)
        st.text("Model Performance:")
        st.text(classification_report(y_test, preds))

        st.write("### ✅ Customer Segmentation & Prediction Complete")
    else:
        st.error(f"Dataset must include these columns: {required_cols}")
