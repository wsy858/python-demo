# -*- coding: utf-8 -*-
from bson import ObjectId
from pymongo import MongoClient
from datetime import datetime


# pip install pymongo
def insert():
    client = MongoClient("192.168.10.128:10000")
    db = client.test
    doc = {"address": {
        "street": "2 Avenue",
        "zipcode": "10075",
        "building": "1480",
        "coord": [-73.9557413, 40.7720266]
    }, "borough": "Manhattan", "cuisine": "Italian", "grades": [
        {
            "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
            "grade": "A",
            "score": 11
        },
        {
            "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
            "grade": "B",
            "score": 17
        }
    ], "name": "Vella", "restaurant_id": "41704620", '_id': ObjectId().__str__()}
    result = db.restaurants.insert_one(doc)
    client.close()
    print result


if __name__ == "__main__":
    insert()
