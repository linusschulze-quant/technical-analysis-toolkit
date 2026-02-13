# =========================
# Imports
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf
from IPython.display import clear_output, display
import os

# =========================
# Constants
# =========================
# Ticker
TICKER: str = "ACM"
# Date range
START_DATE: str = "2010-01-01"
# Number of trading days in a year (used for annualizing)
TRADING_DAYS = 252
# Stock and S&P 500 data
stock = yf.download(TICKER, start=START_DATE)["Close"]
sp500 = yf.download("^GSPC", start=START_DATE)["Close"]