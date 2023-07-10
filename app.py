
import yfinance as yf
from stock import save_dict_as_json, get_ticker_list
from stock_mongo import add_a_stock
import os
from datetime import datetime

# Get the current time
now = datetime.now()

ticker_list = get_ticker_list()
# ticker_list_str = ' '.join(ticker_list)
# tickers = yf.Tickers(ticker_list_str)

info = yf.Ticker(ticker_list[0]).info

if 'recommendationKey' not in info:
    info['recommendationKey'] = 'unknown'
        
#save_dict_as_json(info, os.path.join(dir, tkr+'.json'))
#add_a_stock(s)
#exit(0)

# access each ticker using (example)
dir = './data'

for tkr in ticker_list:
    try:
        print(tkr)
        ticker = yf.Ticker(tkr)

        info = ticker.info if hasattr(ticker, 'info') else {}
        news = ticker.news if  hasattr(ticker, 'news') else {}
        #actions = ticker.actions if hasattr(ticker, 'actions') else {}
        # dividends = ticker.dividends if 'dividends' in ticker else {}
        # splits = ticker.splits if 'splits' in ticker else {}
        #capital_gains = ticker.capital_gains if hasattr(ticker, 'capital_gains') else {}
        #income_stmt = ticker.income_stmt if hasattr(ticker,'income_stmt') else {}
        # quarterly_income_stmt = ticker.quarterly_income_stmt if 'quarterly_income_stmt' in ticker else {}
        # balance_sheet = ticker.balance_sheet if 'balance_sheet' in ticker else {}
        # quarterly_balance_sheet = ticker.quarterly_balance_sheet if 'quarterly_balance_sheet' in ticker else {}
        # cashflow = ticker.cashflow if 'cashflow' in ticker else {}
        # quarterly_cashflow = ticker.quarterly_cashflow if 'quarterly_cashflow' in ticker else {}
        # major_holders = ticker.major_holders if 'major_holders' in ticker else {}
        # institutional_holders = ticker.institutional_holders if 'institutional_holders' in ticker else {}
        # mutualfund_holders = ticker.mutualfund_holders if 'mutualfund_holders' in ticker else {}
        # earnings_dates = ticker.earnings_dates if 'earnings_dates' in ticker else {}
        # isin = ticker.isin if 'isin' in ticker else {}
        # options = ticker.options if 'options' in ticker else {}
        # capital_gains = ticker.capital_gains if 'capital_gains' in ticker else {}

        #save_dict_as_json(info, os.path.join(dir, tkr+'.json'))
        s = {
            'symbol' : tkr,
            'sector': info['sector'] if 'sector' in info else 'unknown',
            'now': now,
            'price' : info['currentPrice'] if 'currentPrice' in info else -1,
            'marketCap' : info['marketCap'] if 'marketCap' in info else -1,
            
            'yf': {
                'buyorsell': info['recommendationKey'] if 'recommendationKey' in info else 'unknown',
                'risk': info['overallRisk'] if 'overallRisk' in info else -1,
                'heldPercentInsiders':  info['heldPercentInsiders'] if  'heldPercentInsiders' in info else -1,
                'heldPercentInstitutions': info['heldPercentInstitutions'] if  'heldPercentInstitutions' in info else -1,
                'profitMargins': info['profitMargins'] if 'profitMargins'in info else -1,
                'operatingCashflow': info['operatingCashflow'] if 'operatingCashflow' in info else -1,
                'earningsGrowth': info['earningsGrowth'] if 'earningsGrowth' in info else -1,
                'totalDebt': info['totalDebt'] if 'totalDebt' in info else -1,
                'info': info,
                'news': news,
            }    
        }
        
        add_a_stock(s)
    except Exception as e:
        print(e)
        

        
print('done')

