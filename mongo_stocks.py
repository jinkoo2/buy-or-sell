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
def stocks():
    client = get_mongo_client()
    return client[db_name].stocks
    
def add_a_stock(obj):
    stock_id = stocks().insert_one(obj).inserted_id
    print(f'stock added id={stock_id}')

def get_the_lastly_added_stock():
    latest_document = stocks().find_one(sort=[("_id", DESCENDING)])
    return latest_document




