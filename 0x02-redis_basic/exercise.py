#!/usr/bin/env python3
""" Writing strings to Redis """


import redis
import typing as t
from uuid import uuid4


class Cache:
    """ Caching class
    """
    def __init__(self) -> None:
        """ creating instance of redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: t.Union[str, bytes, int, float]) -> str:
        """  method that takes a data argument and returns a string. """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: t.Optional[callable] = None) -> any:
        val = self._redis.get(key)
        if not val:
            return
        if fn is int:
            return self.get_int(val)
        if fn is str:
            return self.get_str(val)
        if callable(fn):
            return fn(val)
        return val

    def get_str(self, arg):
        """ converts arg to str """
        return arg.decode('utf-8')

    def get_int(self, arg):
        """ converts arg to int """
        return int(arg)
