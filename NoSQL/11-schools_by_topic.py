#!/usr/bin/env python3
"""
Module to find schools by topic in a MongoDB collection.

This script defines a function to search for schools that have a specific topic
in their "topics" field.
"""

from pymongo.collection import Collection

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection (Collection): pymongo collection object
        topic (str): Topic to search for

    Returns:
        List[dict]: List of documents (schools) that contain the topic
    """
    return list(mongo_collection.find({"topics": topic}))
