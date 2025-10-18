import json

from project.configuration.API_ENDPOINTS import API_ENDPOINTS
from framework.api._api_meta_category import _APImetaCategory


class Product(_APImetaCategory):
    _url = "https://dummyjson.com/products"

    def get_products(self):
        return self.api.client.get(self._url)

    def get_product_by_id(self, product_id):
        return self.api.client.get(self._url + "/" + str(product_id))

    def create_product(self, data):
        return self.api.client.post(API_ENDPOINTS.ADD_PRODUCT, data=json.dumps(data))
