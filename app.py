import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("S&P 500 Consumer Staples Monthly Return & Volatility Tool")
st.subheader("ACC102 Track 4 | WRDS-CRSP 2021-2025")

data = {
    "Year-Month": [
        "2021-01","2021-06","2021-12",
        "2022-01","2022-06","2022-2012",
        "2023-01","2023-06","2023-12",
        "2024-01","2024-06","2024-12",
        "2025-01","2025-06"
    ],
    "Monthly Return (%)": [1.2, 2.1, -0.8, 0.9, -1.3, 0.5, 1.5, 0.7, 1.0, 0.4, 1.8, 0.2, 0.6, 1.1],
    "Monthly Volatility (%)": [3.2, 3.8, 4.5, 4.1, 5.2, 3.5, 2.9, 3.1, 3.0, 2.8, 3.3, 2.7, 2.5, 2.6]
}

df = pd.DataFrame(data)

year = st.selectbox("Select Year", ["All","2021","2022","2023","2024","2025"])
if year != "All":
    df = df[df["Year-Month"].str.startswith(year)]

st.subheader("Monthly Return & Volatility Data")
st.dataframe(df)

st.subheader("Monthly Volatility Trend")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["Year-Month"], df["Monthly Volatility (%)"], marker="o", color="#2E86AB")
ax.set_xlabel("Date")
ax.set_ylabel("Volatility (%)")
plt.xticks(rotation=45)
ax.grid(alpha=0.3)
st.pyplot(fig)

st.subheader("Monthly Return Distribution")
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.bar(df["Year-Month"], df["Monthly Return (%)"], color="#A23B72")
ax2.set_xlabel("Date")
ax2.set_ylabel("Return (%)")
plt.xticks(rotation=45)
st.pyplot(fig2)

st.caption("Source: WRDS-CRSP S&P 500 Sector Database | 2021-2025")