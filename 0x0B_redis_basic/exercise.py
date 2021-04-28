#!/usr/bin/env python3
""" 0x0B. Redis basic
"""
import redis
from typing import Union, Callable, Optional
import uuid


def count_calls(method: Callable) -> Callable:
    """ count_calls method
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ cache class
    """
    def __init__(self):
        """ store redis instance and flush
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method takes data, returns string
        """
        key = str(uuid.uuid1())
        self._redis.mset({key: data})

        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """ convert data back to desired format.
        """
        data = self._redis.get(key)

        return fn(data) if fn else data
