#!/usr/bin/env python3
""" log stats py """
from pymongo import MongoClient


def func():
    """func provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    col = client.logs.nginx

    count = col.count_documents({})

    print(count, 'logs')
    print('Methods:')
    print('\tmethod GET:', col.count_documents({'method': 'GET'}))
    print('\tmethod POST:', col.count_documents({'method': 'POST'}))
    print('\tmethod PUT:', col.count_documents({'method': 'PUT'}))
    print('\tmethod PATCH:', col.count_documents({'method': 'PATCH'}))
    print('\tmethod DELETE:', col.count_documents({'method': 'DELETE'}))
    print(col.count_documents({'path': '/status'}), 'status check')


if __name__ == '__main__':
    func()
