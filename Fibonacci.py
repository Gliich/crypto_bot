import yfinance as yf
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

symbol = 'TRX-USD'
data=yf.Ticker(symbol)
history = data.history(period='1d' , start='2021-01-01')
history['Date'] = history.index
history

plt.figure(figsize=(16,8))
plt.plot(history['Date'] , history['Close'] , linewidth=2)
plt.show()

d = history['2021-07-01' : ]

price_min = d['Close'].min()
print(price_min)


price_max = d['Close'].max()
print(price_max)

diff = price_max - price_min
level1 = price_max - 0.236*diff
level2 = price_max - 0.382*diff
level3 = price_max - 0.618*diff

print('0' , "     " , price_max)
print('0.236' , "   " , level1)
print('0.382' , "   " ,level2)
print('0.618' , "   " , level3)
print('1' , "     " , price_min)

plt.figure(figsize=(16,8))
plt.plot(history['Date'] , history['Close'] , linewidth=2)

plt.axhspan(level1 , price_min , alpha=0.5 , color='lightsalmon')
plt.axhspan(level2 , level1 , alpha=0.5 , color='palegoldenrod')
plt.axhspan(level3 , level2 , alpha=0.5 , color='palegreen')
plt.axhspan(price_max , level3 , alpha=0.5 , color='powderblue')

plt.title('FIBONACCI')
plt.show()
