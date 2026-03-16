import streamlit as st
import plotly.graph_objects as go
import time

from data_fetch import get_stock_data
from analytics import add_indicators

st.title("Real-Time Stock Analytics Dashboard")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

placeholder = st.empty()

while True:

    df = get_stock_data(ticker)
    df = add_indicators(df)

    latest_price = df["Close"].iloc[-1]
    volatility = df["Volatility"].iloc[-1]

    col1, col2 = st.columns(2)

    col1.metric("Current Price", round(latest_price,2))
    col2.metric("Volatility", round(volatility,4))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Datetime"],
        y=df["Close"],
        name="Price"
    ))

    fig.add_trace(go.Scatter(
        x=df["Datetime"],
        y=df["MA20"],
        name="MA20"
    ))

    fig.add_trace(go.Scatter(
        x=df["Datetime"],
        y=df["MA50"],
        name="MA50"
    ))

    placeholder.plotly_chart(fig)

    time.sleep(60)
