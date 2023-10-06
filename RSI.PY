import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download(tickers='ETH-USD' , start= '2020-01-01' , end= '2021-01-01')


def RSI(df,n):
    delta=df['Close'].diff(1)
    delta = delta.dropna()
    up=delta.copy()
    down=delta.copy()
    up[up<0]=0
    down[down>0]=0
    avg_gain=up.rolling(window=n).mean()
    avg_loss=abs(down.rolling(window=n).mean())
    RS = avg_gain/avg_loss
    RSI = 100.0 - (100.0/(1.0+RS))
    return RSI


data = RSI(df,14)
data.dropna()


newdf = pd.DataFrame()
newdf['Close'] = df['Close']
newdf['RSI'] = data



fig , (ax1 , ax2)=plt.subplots(nrows=2 , ncols=1 , figsize=(16,8))
ax1.plot(newdf['Close'],label='Close Price')
ax2.plot(newdf['RSI'],label='RSI')
ax2.axhline(10 , linestyle='--',color='orange',alpha=0.5)
ax2.axhline(20 , linestyle='--',color='green',alpha=0.5)
ax2.axhline(30 , linestyle='--',color='red',alpha=0.5)
ax2.axhline(70 , linestyle='--',color='red',alpha=0.5)
ax2.axhline(80 , linestyle='--',color='green',alpha=0.5)
ax2.axhline(90 , linestyle='--',color='orange',alpha=0.5)
ax1.set_title('RSI Indicator')
plt.show()