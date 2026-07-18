# CODEC_stockmarket-dashboard

# 📈 Real-Time Stock Market Dashboard

A live, interactive web dashboard that tracks and visualizes real-time stock market data, built as part of the CODEC Technologies Software Development Internship.

🔗 **Live Demo:** [https://codecstockmarket-dashboard-f5qyd7rm9sijsa2r6unxxd.streamlit.app/]

## Overview

This dashboard allows users to enter any stock ticker symbol and instantly view live pricing data, historical trends, trading volume, and key technical indicators — all rendered through interactive, real-time charts.

## Features

- 🔍 **Live ticker lookup** — search any publicly traded stock by symbol (e.g. AAPL, TSLA, INFY.NS)
- 💰 **Real-time metrics** — current price, day high/low, trading volume, and percentage change
- 🕯️ **Interactive candlestick chart** — visualize open, high, low, and close prices over a selectable time period
- 📊 **Volume chart** — track trading activity over time
- 📈 **Moving averages** — 20-day and 50-day moving average overlays to identify price trends
- 📋 **Raw data table** — expandable view of the underlying historical price data

## Tech Stack

- **Python** — core application logic
- **Streamlit** — web app framework and UI
- **yfinance** — real-time and historical stock data (Yahoo Finance API wrapper, no API key required)
- **Plotly** — interactive candlestick, volume, and trend charts
- **Pandas** — data processing and moving average calculations

## How It Works

1. User enters a stock ticker symbol and selects a time period/interval in the sidebar
2. The app fetches live and historical data using the `yfinance` library
3. Key metrics (price, change, volume) are calculated and displayed
4. Plotly generates interactive candlestick and volume charts
5. 20-day and 50-day moving averages are calculated using Pandas and overlaid on the price chart

## Screenshots

*(Add your app screenshots here)*

## Running Locally

```bash
git clone https://github.com/dokeabhinav07-work/CODEC_StockMarketDashboard.git
cd CODEC_StockMarketDashboard
pip install -r requirements.txt
streamlit run app.py
```

## Author

ABHINAV ARUN DOKE — CODEC Technologies Software Development Internship

## Acknowledgments

Built using free, open-source tools: Streamlit, yfinance, and Plotly.
