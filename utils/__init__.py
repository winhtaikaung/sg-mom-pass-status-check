"""
Indico Request/Response Utils
"""
import re

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
import json, logging

from error import InvalidJSON, MongoError
from error import CustomError

LOGGER = logging.getLogger("indico")


def mongo_callback(req):
    def decorator(func):
        def wrapper(result, error):
            try:
                if error:
                    raise MongoError(error)
                func(result)
            except CustomError as e:
                req.respond(e.message, e.code)

        return wrapper

    return decorator


def form_urlencoded_parse(body):
    """
    Parse x-www-form-url encoded data
    """
    try:
        data = urlparse.parse_qs(body, strict_parsing=True)
        for key in data:
            data[key] = data[key][0]
        return data
    except ValueError:
        raise InvalidJSON()


def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def smart_parse(body):
    """
    Handle json, fall back to x-www-form-urlencoded
    """
    try:
        data_dict = json.loads(body)
    except ValueError:
        return form_urlencoded_parse(body)
    return data_dict
