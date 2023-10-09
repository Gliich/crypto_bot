import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt 



df = yf.download(tickers='ETH-USD' , start= '2020-01-01' , end= '2021-01-01')
df
def DEMA(data , time_period , column):
    EMA = data[column].ewm(span=time_period , adjust = False).mean()
    DEMA = 2*EMA - EMA.ewm(span=time_period , adjust = False).mean()
    return DEMA


df['DEMA Short'] = DEMA(df,20,'Close')
df['DEMA Long'] = DEMA(df,50,'Close')


plt.style.use('fivethirtyeight')

column_list = ['DEMA Short' , 'DEMA Long' , 'Close']
df[column_list].plot(figsize=(16,8))
plt.title('Close Price & DEMA')
plt.ylabel('USD')
plt.xlabel('Date')
plt.show()



def DEMA_signal(data):
    buy_list = []
    sell_list = []
    flag = False
    for i in range(0, len(data)):
        if data['DEMA Short'][i] > data['DEMA Long'][i] and flag == False:
            buy_list.append(data['Close'][i])
            sell_list.append(np.nan)
            flag = True
        elif data['DEMA Short'][i] < data['DEMA Long'][i] and flag == True:
            buy_list.append(np.nan)
            sell_list.append(data['Close'][i])
            flag = False
            
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)
    data['Buy'] = buy_list
    data['Sell'] = sell_list       

DEMA_signal(df)


plt.figure(figsize=(16,8))

plt.plot(df['Close'], label='Close Price', alpha=0.3)
plt.plot(df['DEMA Short'], label='DEMA Short', alpha=0.3)
plt.plot(df['DEMA Long'], label="DEMA Long", alpha=0.3)

plt.scatter(df.index, df['Buy'], label='BUY Signal',marker='^',color='g')
plt.scatter(df.index, df['Sell'], label='SELL Signal',marker='v',color='r')

plt.xticks(rotation=45)
plt.title(' DEMA Indicator') 
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show() 
