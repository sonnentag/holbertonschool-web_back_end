#!/usr/bin/env python3
""" 8. List  all documents in Python
"""
import pymongo


def list_all(mongo_collection) -> list:
    """ list all documents
    """
    all: list = []
    for doc in mongo_collection.find():
        all.append(doc)

    return all
