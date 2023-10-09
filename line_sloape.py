
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import statsmodels.api as sm



df = yf.download(tickers='ETH-USD' , start= '2020-01-01' , end= '2021-01-01')


def slope(df,n):
    data = df['Close']
    slopes = [i*0 for i in range(n-1)]
    for i in range(n,len(data)+1):
        y = data[i-n:i]
        x = np.array(range(n))
        y_scaled = (y - y.min())/(y.max() - y.min())
        x_scaled = (x - x.min())/(x.max() - x.min())
        x_scaled = sm.add_constant(x_scaled)
        model = sm.OLS(y_scaled,x_scaled)
        results = model.fit()
        slopes.append(results.params[-1])
    slope_angle = (np.rad2deg(np.arctan(np.array(slopes))))
    return np.array(slope_angle)


df['slope'] = slope(df, 5)
df

df.iloc[:,[4,6]].plot(subplots=True , layout = (2,1), figsize=(16,8));
