#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB.

This script connects to a MongoDB database and retrieves statistics
about Nginx logs, including the total number of logs, counts by HTTP method,
and the number of GET requests to /status.
"""

# from pymongo import MongoClient

def log_stats():
    """
    Retrieves and displays statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods statistics
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET requests to /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
