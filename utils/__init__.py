"""
Indico Request/Response Utils
"""

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
import json, logging

from error import MissingField, InvalidJSON, MongoError
from error import CustomError, WrongFieldType

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


def smart_parse(body):
    """
    Handle json, fall back to x-www-form-urlencoded
    """
    try:
        data_dict = json.loads(body)
    except ValueError:
        return form_urlencoded_parse(body)
    return data_dict
