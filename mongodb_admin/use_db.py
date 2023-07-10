from pymongo import MongoClient

server = 'apps.monocycle18.com'
port = 5051

db_name = 'newdb8'
db_user = 'user'
db_password = 'user_password'


# connect to the db
client = MongoClient(f'mongodb://{db_user}:{db_password}@{server}:{port}/{db_name}')

post = {
    "author": "Mike2",
    "text": "My first blog post!",
}

post_id = client[db_name].posts.insert_one(post).inserted_id

print(post_id)

print('done')