#!/usr/bin/env python3
"""
Module to insert a new document in a MongoDB collection.

This script defines a function to insert a document into a MongoDB collection
using the pymongo library. It accepts key-value pairs as input and returns the
_id of the newly inserted document.
"""

from pymongo import Mongoclient

def insert_school(mongo_collection, **kwargs):
    # """
    # Inserts a new document in a MongoDB collection based on kwargs.

    # Args:
    #     mongo_collection (Collection): pymongo collection object
    #     **kwargs: Key-value pairs representing the document fields

    # Returns:
    #     ObjectId: The new document's _id.
    # """
    # new_document = kwargs
    # result = mongo_collection.insert_one(new_document)
    # return result.inserted_id

    """insert a new document in a collection named in kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
