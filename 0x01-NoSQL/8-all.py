#!/usr/bin/env python3
""" Listing all documents in Python """

if __name__ == '__main__':
    def list_all(mongo_collection):
        """ unction that lists all documents in a collection """
        var = list(mongo_collection.find())
        if not var:
            return var
        return var
