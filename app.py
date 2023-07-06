
import yfinance as yf
from stock import save_dict_as_json, get_ticker_list
import os

ticker_list = get_ticker_list()
# ticker_list_str = ' '.join(ticker_list)
# tickers = yf.Tickers(ticker_list_str)

# access each ticker using (example)
dir = './data'

for tkr in ticker_list:
    try:
        print(tkr)
        info = yf.Ticker(tkr).info
        save_dict_as_json(info, os.path.join(dir, tkr+'.json'))

        if 'recommendationKey' in info:
            print(info['recommendationKey'])
        else:
            print('[no recommendation]')
    except:
        print('ERROR!')
        
print('done')

