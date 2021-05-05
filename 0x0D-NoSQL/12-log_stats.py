#!/usr/bin/env python3
""" 12. Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs.nginx
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(db.count_documents({}), "logs")
    print("Methods:")
    for m in method:
        print(f'\tmethod {m}:', db.count_documents({"method": m}))

    print(db.count_documents(
        {"method": "GET", "path": "/status"}),
        "status check"
        )
