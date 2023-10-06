import pandas as pd
import pandas_datareader as wb
import matplotlib.pyplot as plt
import numpy as np


df = wb.DataReader('XRP-USD' , data_source='yahoo' , start = '2020-01-01')
df


def OBV(DF):
    df = DF.copy()
    df['daily ret'] = df['Close'].pct_change()
    df['direction'] = np.where(df['daily ret']>0 , 1 , -1)
    df['direction'][0] = 0
    df['adj vol'] = df['Volume']*df['direction']
    df['obv'] = df['adj vol'].cumsum()
    return df['obv']

data = OBV(df)
data

plt.figure(figsize=(16,8))
ax1 = plt.subplot2grid((11,1) , (0,0) , rowspan = 5 , colspan = 1)
ax2 = plt.subplot2grid((11,1) , (6,0) , rowspan = 5 , colspan = 1)


ax1.plot(df['Close'] , linewidth = 2 , label='Price' , color= '#ff9800')
ax1.set_title('Closing Price')
ax2.plot(data , linewidth = 3 , label='OBV' , color= '#26a69a' , alpha = 0.3)
ax2.set_title('OBV Indicator')
ax1.legend()
ax2.legend()
plt.show()

