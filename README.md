# S&P 500 Consumer Staples Interactive Financial Analysis Dashboard

## 1. Problem & User
This interactive dashboard provides finance students and junior analysts with an intuitive tool to analyze the market performance and financial stability of S&P 500 Consumer Staples companies through customizable filters and visual analytics.

## 2. Data
- Source: Simulated data based on S&P 500 Consumer Staples sector constituents (for academic use only)
- Access Date: N/A (programmatically generated data)
- Key Fields: Company, Year-Month (2021-2025), Monthly Return Percentage, Monthly Volatility Percentage, Total Assets, Total Liabilities, Total Equity, Current Ratio, Debt-to-Asset Ratio

## 3. Methods
1. Generated simulated financial and market data using Python's random library
2. Processed and structured data with Pandas for filtering and aggregation
3. Built an interactive web interface using Streamlit with multi-dimensional filters
4. Created visualizations including trend charts, bar graphs, and correlation heatmaps with Matplotlib
5. Implemented risk metrics, company rankings, data export, and conditional formatting

## 4. Key Findings
- Consumer Staples companies demonstrate stable monthly returns and moderate volatility, consistent with defensive sector characteristics
- Low-leverage companies (Debt-to-Asset Ratio < 0.4) exhibit lower volatility with comparable returns
- Most companies maintain healthy current ratios, indicating strong short-term liquidity
- A weak positive correlation exists between leverage ratio and return volatility
- Sector average returns remained consistent across the 2021-2025 period

## 5. How to run
1. Execute the application: streamlit run app.py

## 6. Product link / Demo
This is a local desktop application. Run the code locally to access the full interactive demo.

## 7. Limitations & next steps
- Limitations: Data is simulated and does not reflect real market events or actual financial statements; limited to 10 companies
- Next steps: Integrate real financial API data, add profitability metrics, build forecasting models, compare with sector ETF benchmarks, deploy to cloud platform
