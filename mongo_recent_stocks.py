from pymongo import MongoClient, DESCENDING
from config import get_config

# config
config = get_config()
db_user = config['db_user']
db_password = config['db_password']
server = config['server']
port = config['port']
db_name = config['db_name']

def get_mongo_client():
    return MongoClient(f'mongodb://{db_user}:{db_password}@{server}:{port}/{db_name}')

# stocks collection
def recent_stocks():
    client = get_mongo_client()
    return client[db_name].recent_stocks

def update_a_stock(obj):
    
    # symbol and 
    symbol = obj['symbol']    
    
    collection = recent_stocks()

    # delete all existing ones of the symbol
    ret = collection.delete_many({"symbol": symbol})
    print(f'mongo_recent_stocks.update_a_stock():stocks of symbol[{symbol}] have been removed', ret)

    # insert the new one
    stock_id = collection.insert_one(obj).inserted_id
    print(f'mongo_recent_stocks.update_a_stock():stock added id={stock_id}')