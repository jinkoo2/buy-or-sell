from pymongo import MongoClient

server = 'apps.monocycle18.com'
port = 5051
db_name = 'stock'
db_user = 'user'
db_password = 'kjk759843'

def get_mongo_client():
    return MongoClient(f'mongodb://{db_user}:{db_password}@{server}:{port}/{db_name}')

def add_a_stock(obj):
    client = get_mongo_client()
    stock_id = client[db_name].stocks.insert_one(obj).inserted_id
    print(f'stock added id={stock_id}')
