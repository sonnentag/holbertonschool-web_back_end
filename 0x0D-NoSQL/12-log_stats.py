#!/usr/bin/env python3
"""
"""
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client.logs.nginx
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print(db.count_documents({}), "logs")
print("Methods:")
for m in method:
    print(f'\tmethod {m}: db.countDocuments()')

print(db.count_documents({"method": "GET", "path": "/status"}) "status check")
