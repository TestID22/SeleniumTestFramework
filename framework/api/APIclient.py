import requests
from framework.api.product import Product

class APIClient:
    url = "https://dummyjson.com/auth/login"

    def __init__(self):
        self.headers = {}
        self.client = requests.Session()

    def autorize(self):
        response = requests.post(url=self.url, data={"username": "emilys", "password": "emilyspass"})  # Mock creds

        if response.status_code != 200:
            raise Exception(response.text + "Credentials are incorrect")

        self.headers = response.json()['accessToken']

    @property
    def products(self):
        return Product(self)

