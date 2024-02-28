#!/usr/bin/env python3
"""
Imports
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert school
    """
    inserted_id = mongo_collection.insert_one(kwargs).inserted_id
    return inserted_id
