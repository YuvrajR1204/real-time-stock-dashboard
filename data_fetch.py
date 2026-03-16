import yfinance as yf
import pandas as pd

def get_stock_data(ticker="AAPL", period="1d", interval="1m"):
    
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)

    df.reset_index(inplace=True)

    return df
