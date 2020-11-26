from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient(host='localhost', username='MongoDB', password='')


def create_collection(db_name: str, collection: str):
    db = client[db_name]
    collection = db[collection]


def add_Sneakers(name: str, count: int, manufacturer: str, price: float, size: int) -> str:
    id = client.Sneakers.insert_one({'name': name, 'count': count, 'manufacturer': manufacturer, 'price': price, 'size': size})
    return id.inserted_id





