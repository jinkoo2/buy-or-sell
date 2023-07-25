from pymongo import MongoClient, DESCENDING
from config import get_config
import utils
from time import time

# config
config = get_config()
db_user = config['db_user']
db_password = config['db_password']
server = config['server']
port = config['port']
db_name = config['db_name']
app_name = config['app_name']

def get_mongo_client():
    return MongoClient(f'mongodb://{db_user}:{db_password}@{server}:{port}/{db_name}')

# stocks collection
def logs():
    client = get_mongo_client()
    return client[db_name].logs

def add_a_log(obj):
    log_id = logs().insert_one(obj).inserted_id

def log(msg):
    add_a_log({
        "t": time(),
        #"host": utils.get_hostname(),
        #"ip" : utils.get_local_ip(),
        "app": app_name,
        "msg": msg
    })