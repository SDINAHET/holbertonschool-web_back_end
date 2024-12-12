#!/usr/bin/env python3
"""
Module to update topics of a school document in a MongoDB collection.

This script defines a function to update the "topics" field of a document
in a MongoDB collection based on the school name.
"""

# from pymongo.collection import Collection

def update_topics(mongo_collection: Collection, name: str, topics: list):
    # """
    # Updates the topics of a school document in the collection based on the name.

    # Args:
    #     mongo_collection (Collection): pymongo collection object
    #     name (str): The school name to update
    #     topics (list): The list of topics to set for the school

    # Returns:
    #     None
    # """
    # mongo_collection.update_many(
    #     {"name": name},
    #     {"$set": {"topics": topics}}
    # )
    """changes all topics of a school document based on the name"""
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
