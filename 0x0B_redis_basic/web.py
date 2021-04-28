#!/usr/bin/env python3
""" 5. Implementing an expiring web cache and tracker
"""
import requests
import redis
from functools import wraps
from typing import Callable

rds = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """ count number of requests called
    """

    @wraps(method)
    def wrapper(url):
        """
        """
        rds.incr(f"count:{url}")
        cached_html = rds.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        rds.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """ obtain HTML content and return it
    """
    ret = requests.get(url)
    return ret.text
