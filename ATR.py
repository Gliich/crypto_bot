
def ATR(DF,n):
    df = DF.copy()
    df['H-L'] = abs(df['High'] - df['Low'])
    df['H-PC']= abs(df['High'] - df['Close'].shift(1))
    df['L-PC']= abs(df['Low'] - df['Close'].shift(1))
    df['TR'] = df[['H-L' , 'H-PC' , 'L-PC']].max(axis=1 , skipna=False)
    df['ATR']=df['TR'].rolling(n).mean()
    df2 = df.drop(['H-L' , 'H-PC' , 'L-PC'] , axis=1)
    return df2
