import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

"""
stock = '^DJI.csv'
stockdf = pd.read_csv(stock)
stockdf = stockdf.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1).rename(columns={'Adj Close': 'Price'})
stockdf.to_csv(stock, index=False)
"""
#"""
mypath = './'
stocks = [f for f in listdir(mypath) if isfile(join(mypath, f))]

slist = []

for stock in stocks:
    if (stock == '.DS_Store' or stock == 'CleanStocks.py'):
        continue
    print(stock)


    '''
    stockdf = pd.read_csv(mypath + stock)
    try:
        stockdf = stockdf.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1).rename(columns={'Adj Close': 'Price'})
        stockdf.to_csv(mypath + stock, index=False)
    except:
        print("ALREAYDDONE")
    '''

    stockdf = pd.read_csv(mypath + stock)
    s = stock.replace('.csv', '')
    stockdf['Symbol'] = stock.replace('.csv', '')
    slist.append(stockdf)

#print(slist)
result = pd.concat(slist)
result.to_csv('pharmstocks.csv', index=False)

#"""