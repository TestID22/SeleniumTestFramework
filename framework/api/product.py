from framework.api._api_meta_category import _APImetaCategory


class Product(_APImetaCategory):
    _url = "https://dummyjson.com/products"

    def get_products(self):
        return self.api.client.get(self._url)

    def get_product_by_id(self, id):
        return self.api.client.get(self._url + "/" + str(id))

    def create_product(self, data):
        _data = json.dumps({'vitalii': 'bmw'})
        self.api.client.post(self._url, data=_data)