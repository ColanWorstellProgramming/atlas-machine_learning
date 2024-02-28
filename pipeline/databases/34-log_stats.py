#!/usr/bin/env python3
"""
Imports
"""
from pymongo import MongoClient


def get_logs_stats():
    """
    get log stats
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    total_logs = collection.count_documents({})

    print(f"first line: {total_logs} logs where {total_logs} is the number of documents in this collection")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{count} logs with method={method}")

    status_logs_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_logs_count} logs with method=GET\npath=/status")
