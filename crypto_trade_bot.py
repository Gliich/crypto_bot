import pandas as pd
import yfinance as yf

symbol = 'TRX-USD'

data = yf.Ticker(symbol)

history = data.history(start='2020-01-01',end='2022-01-01')

history.info()