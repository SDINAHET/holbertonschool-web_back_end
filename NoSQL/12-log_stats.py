#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB.

This script connects to a MongoDB database and retrieves statistics
about Nginx logs, including the total number of logs, counts by HTTP method,
and the number of GET requests to /status.
"""

from pymongo import MongoClient

# def log_stats():
#     """
#     Retrieves and displays statistics about Nginx logs stored in MongoDB.
#     """
#     client = MongoClient('mongodb://127.0.0.1:27017')
#     db = client.logs
#     collection = db.nginx

#     # Total number of logs
#     total_logs = collection.count_documents({})
#     print(f"{total_logs} logs")

#     # Methods statistics
#     print("Methods:")
#     methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
#     for method in methods:
#         count = collection.count_documents({"method": method})
#         print(f"\tmethod {method}: {count}")

#     # Number of GET requests to /status
#     status_check = collection.count_documents({"method": "GET", "path": "/status"})
#     print(f"{status_check} status check")

# if __name__ == "__main__":
#     log_stats()

if __name__ == "__main__":
    """Fournit des statistiques sur les logs nginx"""

    # Connexion à la base de données MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']

    # Liste des méthodes HTTP à analyser
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Affichage du nombre total de logs
    print(f"{collection.count_documents({})} logs")

    # Affichage du nombre de logs pour chaque méthode HTTP de la liste
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Affichage du nombre de logs avec méthode GET et au chemin /status
    print(collection.count_documents({"method": "GET", "path": "/status"}),
          "status check")

    # Fermeture de la connexion à la base de données MongoDB
    client.close()
