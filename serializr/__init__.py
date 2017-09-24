import uuid

from model.merchant import Merchant


def as_merchant(d):
    m = Merchant()
    m.__dict__.update(d)
    m.id = str(uuid.uuid4().hex)
    m.merchant_id = d.get('id')
    return m
