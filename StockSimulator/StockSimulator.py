import os
import math
import warnings
import numpy as np
import pandas as pd
import datetime as dt
import pandas_datareader as web
warnings.filterwarnings("ignore")

class StockSimulator(object):
    def __init__(self):
        prices = pd.read_csv("Prices.csv", index_col="Date", parse_dates=True)
        volumechanges = pd.read_csv("Volume.csv", index_col="Date", parse_dates=True).pct_change() * 100
        today = dt.date(2010, 1, 1)  # Start date of simulation, changes as the simulation iterates towards the end.
        simend = dt.date(2016, 1, 1) # End date of simulation
        tickers = []        # List of stocks to trade
        transactionid = 0   # Transaction ID for each transaction
        money = 100000      # Starting amount of money
        portfolio = {}      # Dictionary of stocks and their quantities
        activelog = []      # List of open positions
        transactionlog = [] # List of transactions
    
    @classmethod
    def download_data(self, cls):
        stocks = []
        if os.path.isfile("SmallStockList.txt"):
            with open("SmallStockList.txt") as f:
                for line in f:
                    stocks.append(line.strip())
            return stocks
        else:
            web.DataReader(stocks, 'yahoo', start='1/1/2010', end='1/1/2016')['Adj Close'].to_csv("Prices.csv")
            web.DataReader(stocks, 'yahoo', start='1/1/2010', end='1/1/2016')['Volume'].to_csv("Volumes.csv")        
            return cls.download_data()
            
