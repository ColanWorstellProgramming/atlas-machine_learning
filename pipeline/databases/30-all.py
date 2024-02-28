#!/usr/bin/env python3
"""
Imports
"""


def list_all(mongo_collection):
    """
    list all
    """
    all_documents = []

    cursor = mongo_collection.find({})

    for document in cursor:
        all_documents.append(document)

    return all_documents
