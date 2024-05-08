import json

import pytest
import requests
from helpers import create_store_name,  create_item_data


class TestItem:
    ENDPOINT = 'items'

    @pytest.fixture()
    def create_item(self, url, create_store):
        data = create_item_data(create_store['id'])
        response = requests.post(f"{url}/{self.ENDPOINT}", data=json.dumps(data))
        return response.json()

    def test_create_item(self, url, create_store):
        store_id = create_store['id']
        data = create_item_data(store_id)
        response = requests.post(f"{url}/{self.ENDPOINT}", data=json.dumps(data))
        assert response.status_code == 201

    def test_get_item(self, url, create_item):
        response = requests.get(f"{url}/{self.ENDPOINT}/{create_item['id']}")
        assert response.status_code == 200

    def test_delete_item(self, url, create_item):
        response = requests.delete(f"{url}/{self.ENDPOINT}/{create_item['id']}")
        assert response.status_code == 200



class TestStore:
    ENDPOINT = 'stores'

    def test_create_store(self, url):
        name = create_store_name()
        response = requests.post(f"{url}/{self.ENDPOINT}", data=json.dumps({"name": name}))
        assert response.status_code == 201
        print(response.text)

    def test_get_store(self, create_store, url):
        store_id = create_store['id']
        response = requests.get(f"{url}/{self.ENDPOINT}/{store_id}")
        assert response.status_code == 200
        print(response.text)

    def test_delete_store(self, create_store, url):
        store_id = create_store['id']
        response = requests.delete(f"{url}/{self.ENDPOINT}/{store_id}")
        assert response.status_code == 200
        print(response.text)
