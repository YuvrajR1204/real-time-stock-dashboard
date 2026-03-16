import pandas as pd

def add_indicators(df):

    df["MA20"] = df["Close"].rolling(window=20).mean()
    df["MA50"] = df["Close"].rolling(window=50).mean()

    df["Returns"] = df["Close"].pct_change()

    df["Volatility"] = df["Returns"].rolling(window=20).std()

    return df
