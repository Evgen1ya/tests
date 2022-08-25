import requests
import pytest

class TestAPI():
    URL = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {'Content-Type': 'application/json',
            'Authorization': 'токен'}
    params = {"path": "pytest", "overwrite": "true"}
    params_response = {"path": "netology", "overwrite": "true"}

    def test_response(self):
        result = requests.get(TestAPI.URL, params=TestAPI.params_response, headers=TestAPI.headers)
        assert 200 == result.status_code

    def test_add(self):
        result = requests.put(TestAPI.URL, params=TestAPI.params, headers=TestAPI.headers)
        assert 201 == result.status_code

