import uuid
from random import randint


def create_store_name():
    return f'testing_{randint(0, 10000)}'


def create_item_data(store_id=None):
    return {
        "name": f'testing_{randint(0, 10000)}',
        "price": 100,
        "description": "lalala",
        "store_id": store_id
    }
