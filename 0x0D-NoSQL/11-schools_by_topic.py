#!/usr/bin/env python3
""" 11. Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """  returns list of school by topic
    """
    results: list = []
    spec: dict = {"topic": topic}

    for result in mongo_collection.find(spec):
        results.append(result)

    return results
