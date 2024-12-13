#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB.

This script connects to a MongoDB database and retrieves statistics
about Nginx logs, including the total number of logs, counts by HTTP method,
and the number of GET requests to /status.
"""

from pymongo import MongoClient


if __name__ == "__main__":
    """Provides statistics about Nginx logs."""

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']

    # Display total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # List of HTTP methods to analyze
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # # Display total number of logs
    # total_logs = collection.count_documents({})
    # print(f"{total_logs} logs")

    # Display the count of logs for each HTTP method
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Display the count of logs with method GET and path /status
    status_check_count = collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{status_check_count} status check")

    # Close the MongoDB connection
    # client.close()
