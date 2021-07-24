import time
import datetime as DT
from binance.client import Client
from binance.enums import *
import pandas as pd
import numpy as np

def megacal(tr1,tr2):

    def computeRSI (data, time_window):
        diff = np.diff(data)
        up_chg = 0 * diff
        down_chg = 0 * diff
    
        
        up_chg[diff > 0] = diff[ diff>0 ]
    
        
        down_chg[diff < 0] = diff[ diff < 0 ]

        up_chg = pd.DataFrame(up_chg)
        down_chg = pd.DataFrame(down_chg)
    
        up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
        down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    
        rs = abs(up_chg_avg/down_chg_avg)
        rsi = 100 - 100/(1+rs)
        rsi = int(rsi[0].iloc[-1])
        return rsi


    api_key = ''
    api_secret = ''



    client = Client(api_key, api_secret)

    trdPair1 = tr1
    trdPair2 = tr2


    tradePair = trdPair1 + trdPair2    
    price = client.get_ticker(symbol=tradePair)
    lastprice = price['askPrice']
    symbol = price['symbol']

    klines = client.get_klines(symbol=tradePair, interval='1m', limit='500')
    klines2 = client.get_historical_klines(tradePair, Client.KLINE_INTERVAL_1DAY, "1 day ago UTC")
    close = [float(entry[4]) for entry in klines]
    close_array = np.asarray(close)
    close_finished = close_array[:-1]
    rsi = computeRSI (close_finished, 14)


    def printinfo():
        print("---------------------------")
        print("process = " +symbol)
        print( "price = " + lastprice + " " +trdPair2)

    def rsibaby():
        if rsi <30:
            return("RSI = Buy")
        if rsi >70:
            return("RSI = Sell")
        else:
            return("RSI = Hodl")
            

        
    
    return("--------------------------------------------------------"+"\n Process = "+symbol+" \n Price = " + lastprice + " " + trdPair2 + "\n " + rsibaby() +"\n --------------------------------------------------------")
