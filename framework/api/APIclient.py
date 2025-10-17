import requests

from framework.api.product import Product


class APIClient:
    url = "https://dummyjson.com/auth/login"

    def __init__(self):
        self._headers = {}
        self.client = requests.Session()

    def authorize(self):
        response = requests.post(url=self.url, data={"username": "emilys", "password": "emilyspass"})  # Mock creds

        if response.status_code != 200:
            raise Exception(response.text + "Credentials are incorrect")
        self._headers['Content-Type'] = 'application/json'
        self._headers['accessToken'] = response.json()['accessToken']

    @property
    def products(self):
        return Product(self)

