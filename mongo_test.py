from pprint import pprint
import pymongo
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['mongo']
user_col = db['users']


users = user_col.find()
user = user_col.find_one(
    {"name": "David"}
)

pprint(user)

user_col.update_one(

    {"name": "Mark"},
    {"$set": {"company": "Apple"}}
)

users = user_col.find()
pprint(list(users))



#pprint(list(users))