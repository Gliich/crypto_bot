import pandas as pd
import pandas_datareader as wb
import matplotlib.pyplot as plt

df = wb.DataReader('BTC-USD' , data_source='yahoo',start='2020-01-01')

def BollingerBand(data,n):
    hlc_avg = (data.High + data.Low + data.Close)/3
    MA = hlc_avg.rolling(n).mean()
    std = hlc_avg.rolling(n).std()
    upper , lower = MA+std*2 , MA - std*2
    return upper , lower

df['BB UP'] , df['BB DOWN'] = BollingerBand(df,20)

df = df.dropna()

plt.rcParams['figure.figsize'] = (20,10)
ax = df[['Close' , 'BB UP' , 'BB DOWN']].plot(color = ['red' , 'grey' , 'grey'])
ax.fill_between(df.index , df['BB UP'] , df['BB DOWN'] , facecolor='orange' , alpha = 0.1)
plt.show()