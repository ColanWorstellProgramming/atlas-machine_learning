#!/usr/bin/env python3
"""
Imports
"""


def schools_by_topic(mongo_collection, topic):
    """
    schools by topic
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
