#!/usr/bin/env python3
""" Writing strings to Redis """


import redis as rds
import typing as t
from uuid import uuid4


class Cache:
    """ Caching class
    """
    def __init__(self) -> None:
        """ creating instance of redis client"""
        self._redis: rds.Redis = rds.Redis()
        self._redis.flushdb()

    def store(self, data: t.Union[str, bytes, int, float]) -> str:
        """  method that takes a data argument and returns a string. """
        id: str = str(uuid4())
        self._redis.set(id, data)
        return id
