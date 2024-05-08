import pytest
import requests

from helpers import create_store_name
from config import URL
import json


@pytest.fixture
def create_store():
    name = create_store_name()
    response = requests.post(f"{URL}/stores", data=json.dumps({"name": name}))
    return response.json()
