import pytest
import requests

from helpers import create_store_name
import json

import os


@pytest.fixture(scope='session')
def url():
    app_url = os.getenv('APP_URL', 'http://127.0.0.1:9000')
    return app_url


@pytest.fixture
def create_store(url):
    name = create_store_name()
    response = requests.post(f"{url}/stores", data=json.dumps({"name": name}))
    return response.json()
