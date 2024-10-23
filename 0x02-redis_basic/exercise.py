#!/usr/bin/python3
""" Writing strings to Redis """


import redis as rds
from uuid import uuid4
import typing as t


class Cache:
    """  class  Cache  """
    def __init__(self) -> None:
        """ creating instance of redis client"""
        self._redis = rds.Redis()
        self._redis.flushdb()

    def store(self, data: t.Union[str, bytes, int, float]) -> str:
        """  method that takes a data argument and returns a string. """
        id: str = str(uuid4())
        self._redis.set('{}'.format(id), data)
        return id
