import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="S&P 500 Consumer Staples Analysis", layout="wide")
st.title("S&P 500 Consumer Staples Sector")
st.subheader("Monthly Return & Volatility Analysis Tool | ACC102 Track 4")

# Representative sample of S&P 500 Consumer Staples constituents
data = {
    "Company": [
        "Procter & Gamble", "Procter & Gamble",
        "Coca-Cola", "Coca-Cola",
        "Walmart", "Walmart",
        "PepsiCo", "PepsiCo",
        "Johnson & Johnson", "Johnson & Johnson",
        "Costco", "Costco",
        "Mondelez", "Mondelez",
        "Colgate-Palmolive", "Colgate-Palmolive",
        "Kroger", "Kroger",
        "Philip Morris", "Philip Morris"
    ],
    "Year-Month": [
        "2023-06", "2024-06",
        "2023-06", "2024-06",
        "2023-06", "2024-06",
        "2023-06", "2024-06",
        "2023-06", "2024-06",
        "2023-06", "2024-06",
        "2023-06", "2024-06",
        "2023-06", "2024-06",
        "2023-06", "2024-06",
        "2023-06", "2024-06"
    ],
    "Monthly_Return_Pct": [
        1.5, 1.8, 1.2, 1.4, 0.9, 1.1,
        1.3, 1.6, 1.0, 1.2, 0.8, 1.0,
        1.1, 1.5, 0.7, 0.9, 0.6, 0.8,
        1.2, 1.4
    ],
    "Monthly_Volatility_Pct": [
        2.9, 2.6, 3.1, 2.8, 2.7, 2.5,
        3.0, 2.7, 2.8, 2.6, 2.4, 2.3,
        2.9, 2.7, 2.6, 2.5, 2.8, 2.6,
        3.2, 2.9
    ]
}

df = pd.DataFrame(data)
df["Year"] = df["Year-Month"].str[:4]

# Side[:4]

# Sidebar filters
st.sidebar.header("Control Panel")
companies = sorted(df["Company"].unique())
selected_companies = st.sidebar.multiselect("Select Companies", companies, default=companies)

years = sorted(df["Year"].unique())
selected_years = st.sidebar.multiselect("Select Years", years, default=years)

vol_min, vol_max = st.sidebar.slider("Volatility Range (%)", 2.0, 4.0, (2.0, 4.0))
ret_min, ret_max = st.sidebar.slider("Return Range (%)", 0.0, 2.0, (0.0, 2.0))

# Filter data
filtered = df[
    df["Company"].isin(selected_companies) &
    df["Year"].isin(selected_years) &
    df["Monthly_Volatility_Pct"].between(vol_min, vol_max) &
    df["Monthly_Return_Pct"].between(ret_min, ret_max)
]

# Summary metrics
st.subheader("Summary Statistics")
c1, c2, c3 = st.columns(3)
c1.metric("Selected Firms", len(selected_companies))
c2.metric("Avg Return", f"{filtered['Monthly_Return_Pct'].mean():.2f}%")
c3.metric("Avg Volatility", f"{filtered['Monthly_Volatility_Pct'].mean():.2f}%")

# Data table
st.subheader("Filtered Data
