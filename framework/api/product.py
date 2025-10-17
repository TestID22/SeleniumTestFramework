from framework.api._api_meta_category import _APImetaCategory


class Product(_APImetaCategory):
    _url = "https://dummyjson.com/products"

    def get_products(self):

        return self.api.client.get(self._url)