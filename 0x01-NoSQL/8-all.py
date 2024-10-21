#!/usr/bin/env python3
""" Listing all documents in Python """


def list_all(mongo_collection):
    """ unction that lists all documents in a collection """
    return mongo_collection.find()
