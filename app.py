import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Real-Time Stock Dashboard", layout="wide")

st.title("📈 Real-Time Stock Market Dashboard")
st.markdown("Track live stock prices, trends, and key financial indicators.")

st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g. AAPL, TSLA, INFY.NS)", value="AAPL")
period = st.sidebar.selectbox("Time Period", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=2)
interval = st.sidebar.selectbox("Interval", ["1d", "1wk", "1mo"], index=0)

if ticker:
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period, interval=interval)

        if data.empty:
            st.error(f"No data found for ticker '{ticker}'. Please check the symbol and try again.")
        else:
            info = stock.info
            company_name = info.get("longName", ticker)
            current_price = data["Close"].iloc[-1]
            prev_close = info.get("previousClose", data["Close"].iloc[-2] if len(data) > 1 else current_price)
            change = current_price - prev_close
            pct_change = (change / prev_close) * 100 if prev_close else 0

            st.subheader(f"{company_name} ({ticker.upper()})")

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Current Price", f"${current_price:.2f}", f"{change:+.2f} ({pct_change:+.2f}%)")
            col2.metric("Day High", f"${data['High'].iloc[-1]:.2f}")
            col3.metric("Day Low", f"${data['Low'].iloc[-1]:.2f}")
            col4.metric("Volume", f"{data['Volume'].iloc[-1]:,.0f}")

            fig = go.Figure()
            fig.add_trace(go.Candlestick(
                x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],
                name=ticker
            ))
            fig.update_layout(
                title=f"{ticker.upper()} Price Chart",
                xaxis_title="Date",
                yaxis_title="Price (USD)",
                xaxis_rangeslider_visible=False,
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("Volume Over Time")
            fig_vol = go.Figure()
            fig_vol.add_trace(go.Bar(x=data.index, y=data['Volume'], marker_color='indianred'))
            fig_vol.update_layout(height=300, xaxis_title="Date", yaxis_title="Volume")
            st.plotly_chart(fig_vol, use_container_width=True)

            st.subheader("Key Financial Indicators")
            data['MA20'] = data['Close'].rolling(window=20).mean()
            data['MA50'] = data['Close'].rolling(window=50).mean()

            fig_ma = go.Figure()
            fig_ma.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Close Price', line=dict(color='blue')))
            fig_ma.add_trace(go.Scatter(x=data.index, y=data['MA20'], name='20-Day MA', line=dict(color='orange')))
            fig_ma.add_trace(go.Scatter(x=data.index, y=data['MA50'], name='50-Day MA', line=dict(color='green')))
            fig_ma.update_layout(height=400, xaxis_title="Date", yaxis_title="Price (USD)")
            st.plotly_chart(fig_ma, use_container_width=True)

            with st.expander("View Raw Data Table"):
                st.dataframe(data[['Open', 'High', 'Low', 'Close', 'Volume']].sort_index(ascending=False))

    except Exception as e:
        st.error(f"Error fetching data: {e}")

st.sidebar.markdown("---")
st.sidebar.markdown("Built with Streamlit, yfinance, and Plotly")
