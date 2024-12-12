#!/usr/bin/env python3


from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents in the collection or an empty list if none.
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
