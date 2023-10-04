
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt 


df = yf.download(tickers='ETH-USD' , start= '2020-01-01' , end= '2021-01-01')
df


def ATR(DF,n):
    df = DF.copy()
    df['H-L'] = abs(df['High'] - df['Low'])
    df['H-PC']= abs(df['High'] - df['Close'].shift(1))
    df['L-PC']= abs(df['Low'] - df['Close'].shift(1))
    df['TR'] = df[['H-L' , 'H-PC' , 'L-PC']].max(axis=1 , skipna=False)
    df['ATR']=df['TR'].rolling(n).mean()
    df2 = df.drop(['H-L' , 'H-PC' , 'L-PC'] , axis=1)
    return df2



def ADX(DF,n):
    
    df2 = DF.copy()
    df2['TR'] = ATR(df2,n)['TR'] 
    
    df2['DMplus']=np.where((df2['High']-df2['High'].shift(1))>(df2['Low'].shift(1)-df2['Low']),
                           df2['High']-df2['High'].shift(1),0)
    
    df2['DMplus']=np.where(df2['DMplus']<0,0,df2['DMplus'])
    
    df2['DMminus']=np.where((df2['Low'].shift(1)-df2['Low'])>(df2['High']-df2['High'].shift(1)),
                            df2['Low'].shift(1)-df2['Low'],0)
    
    df2['DMminus']=np.where(df2['DMminus']<0,0,df2['DMminus'])
    
    TRn = []
    DMplusN = []
    DMminusN = []
    TR = df2['TR'].tolist()
    DMplus = df2['DMplus'].tolist()
    DMminus = df2['DMminus'].tolist()
    
    for i in range(len(df2)):
        if i < n:
            TRn.append(np.NaN)
            DMplusN.append(np.NaN)
            DMminusN.append(np.NaN)
        elif i == n:
            TRn.append(df2['TR'].rolling(n).sum().tolist()[n])
            DMplusN.append(df2['DMplus'].rolling(n).sum().tolist()[n])
            DMminusN.append(df2['DMminus'].rolling(n).sum().tolist()[n])
        elif i > n:
            TRn.append(TRn[i-1] - (TRn[i-1]/14) + TR[i])
            DMplusN.append(DMplusN[i-1] - (DMplusN[i-1]/14) + DMplus[i])
            DMminusN.append(DMminusN[i-1] - (DMminusN[i-1]/14) + DMminus[i])
    
    df2['TRn'] = np.array(TRn)
    df2['DMplusN'] = np.array(DMplusN)
    df2['DMminusN'] = np.array(DMminusN)
    df2['DIplusN']=100*(df2['DMplusN']/df2['TRn'])
    df2['DIminusN']=100*(df2['DMminusN']/df2['TRn'])
    df2['DIdiff']=abs(df2['DIplusN']-df2['DIminusN'])
    df2['DIsum']=df2['DIplusN']+df2['DIminusN']
    df2['DX']=100*(df2['DIdiff']/df2['DIsum'])
    
    ADX = []
    DX = df2['DX'].tolist()
    
    for j in range(len(df2)):
        if j < 2*n-1:
            ADX.append(np.NaN)
        elif j == 2*n-1:
            ADX.append(df2['DX'][j-n+1:j+1].mean())
        elif j > 2*n-1:
            ADX.append(((n-1)*ADX[j-1] + DX[j])/n)
    
    df2['ADX']=np.array(ADX)
    return df2



data = ADX(df,14)

plt.figure(figsize=(16,8))

ax1 = plt.subplot2grid((11,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((11,1), (6,0), rowspan = 5, colspan = 1)

ax1.plot(data['Close'], linewidth = 2, color = '#ff9800')
ax1.set_title('CLOSING PRICE')

ax2.plot(data['DIplusN'], color = '#26a69a', label = '+ DI', linewidth = 3, alpha = 0.3)
ax2.plot(data['DIminusN'], color = '#f44336', label = '- DI', linewidth = 3, alpha = 0.3)
ax2.plot(data['ADX'], color = '#2196f3', label = 'ADX', linewidth = 3)
ax2.axhline(25, color = 'grey', linewidth = 2, linestyle = '--')

ax2.legend()
ax2.set_title('ADX Indicator')
plt.show()




