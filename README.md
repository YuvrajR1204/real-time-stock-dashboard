# Real-Time Stock Analytics Dashboard

## Overview

This project builds a **real-time stock analytics dashboard** that fetches live market data, calculates financial indicators, and visualizes stock trends through an interactive dashboard.

The application allows users to enter a stock ticker and instantly analyze the stock’s performance using moving averages and volatility indicators.

---

## Live Demo

If deployed using Streamlit Cloud:

```
https://your-app-name.streamlit.app
```

---

## Features

* Real-time stock data using Yahoo Finance API
* Interactive price chart
* Moving Average indicators (MA20, MA50)
* Volatility calculation
* User-input ticker search
* Auto-refreshing dashboard

---

## Tech Stack

Python libraries used in this project:

* pandas — data manipulation and analysis
* yfinance — stock market data API
* streamlit — dashboard framework
* plotly — interactive visualizations

---

## Project Structure

```
real-time-stock-dashboard
│
├── app.py
├── data_fetch.py
├── analytics.py
├── requirements.txt
└── README.md
```

### File Description

**app.py**
Main Streamlit dashboard application.

**data_fetch.py**
Handles fetching stock data from Yahoo Finance.

**analytics.py**
Contains calculations for indicators like moving averages and volatility.

**requirements.txt**
Lists the required Python libraries.

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/real-time-stock-dashboard.git
```

Navigate to the project folder:

```
cd real-time-stock-dashboard
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Run the dashboard locally:

```
streamlit run app.py
```

After running the command, the dashboard will open in your browser.

---

## Example Analytics

The dashboard calculates financial indicators such as:

### Moving Averages

Used to smooth price trends and identify direction.

Example:

* MA20 → short-term trend
* MA50 → medium-term trend

### Volatility

Measures how much the stock price fluctuates.

Higher volatility indicates greater market uncertainty.

---

## Future Improvements

Possible upgrades for this project:

* Multi-stock comparison dashboard
* Technical indicators (RSI, MACD)
* Machine learning price prediction
* Portfolio performance tracking

---

## Author

Yuvraj Reddy
Graduate Student | Data Analytics | Machine Learning
