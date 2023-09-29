import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


symbol = 'TRX-USD'
data = yf.Ticker(symbol)
history = data.history(start='2021-01-01',end='2022-01-01')
history


def MACD(DF,a,b,c):
    df=DF.copy()
    df['MA FAST'] = df['Close'].ewm(span=a , min_periods = a).mean()
    df['MA SLOW'] = df['Close'].ewm(span=b , min_periods = b).mean()
    df['MACD'] = df['MA FAST'] - df['MA SLOW']
    df['Signal'] = df['MACD'].ewm(span= c , min_periods = c).mean()  
    df.dropna(inplace=True)
    return df


fig , (ax0 , ax1) = plt.subplots(nrows=2 , ncols=1 , sharex=True , sharey=False , figsize=(16,8))

history.iloc[: , 4].plot(ax=ax0)
ax0.set(ylabel='Price')


history.iloc[: , [-2,-1]].plot(ax=ax1)
ax1.set(xlabel='Date' , ylabel='MACD')

fig.suptitle('MACD Indicator')

plt.plot(history)