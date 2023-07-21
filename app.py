
import yfinance as yf
from stock import save_dict_as_json, get_ticker_list
from stock_mongo import add_a_stock, get_the_lastly_added_stock
import os
from datetime import datetime
import math
import time
import concurrent.futures


def run_one(count):
    ticker_list = get_ticker_list()
    N = len(ticker_list)
    print('N=', N)

    # find the last added symbol
    lastly_added_stock = get_the_lastly_added_stock()
    print('lastly_added_stock=', lastly_added_stock['symbol'])

    if lastly_added_stock is None:
        i_start = 0
    else:
        i_start = ticker_list.index(lastly_added_stock['symbol'])+1
    
        # if 
        if i_start == len(ticker_list):
            i_start =0

    i_end = i_start+count

    if i_end > N:
        i_end = N

    for idx in range(i_start, i_end):
        tkr = ticker_list[idx]
        try:
            print(f'[{idx}/{N}] {datetime.now()} - {tkr}')
            ticker = yf.Ticker(tkr)

            info = ticker.info if hasattr(ticker, 'info') else {}

            try:
                news = ticker.news if  hasattr(ticker, 'news') else {}
            except Exception as e:
                print('no news')
                news = {}

        
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
                'now': datetime.now(),
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

def run_tickers(ticker_list, start_index, last_index):
    N = len(ticker_list)

    for idx, tkr in enumerate(ticker_list):
        try:
            print(f'[{idx+start_index}/{last_index}] {datetime.now()} - {tkr}')
            ticker = yf.Ticker(tkr)

            info = ticker.info if hasattr(ticker, 'info') else {}

            try:
                news = ticker.news if  hasattr(ticker, 'news') else {}
            except Exception as e:
                print('no news')
                news = {}

        
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
                'now': datetime.now(),
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


def get_tickers_of_page(ticker_list, page_num, items_per_page):
    i_start = page_num * items_per_page
    i_end = i_start+items_per_page
    if i_end > len(ticker_list):
        i_end = len(ticker_list)
    return ticker_list[i_start:i_end]

def run_once2():
    ticker_list = get_ticker_list()
    items_per_page = 100
    N = len(ticker_list)
    num_of_pages = math.floor(N/items_per_page)+1

    # create a thread pool with 2 threads
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    for page_num in range(num_of_pages):
        tickers_of_page = get_tickers_of_page(ticker_list, page_num, items_per_page)
        pool.submit(run_tickers, tickers_of_page, page_num * items_per_page, N)


    # wait for all tasks to complete
    pool.shutdown(wait=True)

    print("Main thread continuing to run")
    print('done')


i=0
while True:
    time1 = time.time()
    run_once2()
    time2 = time.time()
    execution_time = time2 - time1
    print(f"Execution time: {i}th run - {execution_time} seconds")
    print('sleeping for 5 minutes...')
    time.sleep(60 * 5)
    i=i+1
