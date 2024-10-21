#!/usr/bin/env python3
""" Insert a document in Python """

if __name__ == '__main__':
    def insert_school(mongo_collection, **kwargs):
        """ function that inserts a new document
        in a collection based on kwargs """
        x = mongo_collection.insert_one(kwargs)
        return x.inserted_id
