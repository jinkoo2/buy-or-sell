from pymongo import MongoClient
import os



server = 'apps.monocycle18.com'
port = 5051

root_username = os.environ.get('MONGODB_ROOT_USERNAME')
root_password = os.environ.get('MONGODB_ROOT_PASSWORD')

db_name = 'stock'
db_user = 'user'
db_password = 'kjk759843'

# connect to the server as root
client = MongoClient(f'mongodb://{root_username}:{root_password}@{server}:{port}')

# add a user to the new db
client[db_name].command('createUser', db_user, pwd=db_password, roles=[{'role': 'readWrite', 'db': db_name}])

print('done')