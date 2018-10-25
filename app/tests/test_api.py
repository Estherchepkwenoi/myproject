import unittest,json
from app.models.products import Products, Product
from app.models.sales import Sales
from app.views import views
from app import app


class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()

    def test_add_product(self):
        """tests if a product has been added"""
        product = {"name" : "sugar",
                   "price" : 10000,
                   "quantity": 2,}
                          
        with self.client as client:
            response = client.post("/api/v1/products", data=json.dumps(product),\
            content_type='application/json')
            self.assertEqual(response.status_code, 201)

    def test_get_products(self):
        with self.client as client:
            response = client.get("/api/v1/products")
            self.assertEqual(response.status_code, 200)

    def test_get_a_product(self):
        with self.client as client:
            response = client.get("/api/v1/products/<id>")
            self.assertEqual(response.status_code, 200)

    def test_product_not_found(self):
        with self.client as client:
            client.post("api/v1/products", json=dict(name="sugar",
            price=10000,quantity=2))
            client.post("api/v1/products", json=dict(name="salt",
            price=1000,quantity=1,))
            response = client.get("/api/v1/products/100")
            self.assertEqual(response.status_code, 404)

    def test_post_sale_order(self):
        with self.client as client:
            response = client.post("/api/v1/sales", json=dict(name='salt',
            price=1000, quantity=1,totalcost=1000,attendant='esther'))
            self.assertEqual(response.status_code, 201)

    def test_get_sale_orders(self):
        with self.client as client:
            response = client.get("/api/v1/sales")
            self.assertEqual(response.status_code, 200)

    def test_get_a_sale_order(self):
        with self.client as client:
            client.post("/api/v1/sales", json=dict(name='sugar', price=5000, quantity=4,totalcost=20000,attendant='esther'))
            client.post("/api/v1/sales", json=dict(name='salt', price=1000, quantity=2,totalcost=2000,attendant='peter'))
            response = client.get("/api/v1/sales/2")
            self.assertEqual(response.status_code, 200)

    def test_sale_order_not_found(self):
        with self.client as client:
            client.post("/api/v1/sales", json=dict(name='sugar',price=5000, quantity=2,totalcost=1000,attendant='esther'))
            client.post("/api/v1/sales", json=dict(name='salt', price=1000, quantity=1,totalcost=1000,attendant='peter'))
            response = client.get("/api/v1/sales/10")
            self.assertEqual(response.status_code, 404)

    def test_product_with_alphabet_only(self):
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="123***", \
            price=5000, category="mens clothing", quantity=10, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_price_not_string(self):
        """tests if price is not a string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price="5000", category="mens clothing", quantity=10, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_price_is_integer(self):
        """tests if price is an integer"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=3.5, category="mens clothing", quantity=10, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_quantity_not_string(self):
        """tests if quantity is not a string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="mens clothing", quantity="ten", minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_quantity_is_integer(self):
        """tests if quantity is not a string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="mens clothing", quantity=10.677, minimum_quantity=5))
            self.assertEqual(response.status_code, 400)

    def test_min_quantity_not_string(self):
        """tests if minimum_quantity is not a string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="mens clothing", quantity=10, minimum_quantity="five"))
            self.assertEqual(response.status_code, 400)

    def test_min_quantity_integer(self):
        """tests if minimum quantity is an integer"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="mens clothing", quantity=10, minimum_quantity=6.8))
            self.assertEqual(response.status_code, 400)

    def test_category_not_empty_string(self):
        """tests if category is not an empty string"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, category="    ", quantity=10, minimum_quantity=6))
            self.assertEqual(response.status_code, 400)

    def test_key_error_post_product(self):
        """tests for keyError when a key is missing"""
        with self.client as client:
            response = client.post("api/v1/products", json=dict(product_name="vest", \
            price=5000, quantity=10, minimum_quantity=6))
            self.assertEqual(response.status_code, 400)

            #validating sale order inputs
    def test_product_name_not_empty_string(self):
        """tests if product_name posted is not an empty string"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name=" ", \
            price=5000, quantity=10))
            self.assertEqual(response.status_code, 400)

    def test_product_name_with_alphabet_only(self):
        """tests if product_name has alphabets only"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="123***", \
            price=5000, quantity=1))
            self.assertEqual(response.status_code, 400)

    def test_sale_price_not_string(self):
        """tests if sale price is not a string"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="vest", \
            price="5000", quantity=1))
            self.assertEqual(response.status_code, 400)

    def test_sale_price_is_integer(self):
        """tests if sale price is an integer"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="vest", \
            price=3.5, quantity=1))
            self.assertEqual(response.status_code, 400)

    def test_sale_quantity_not_string(self):
        """tests if quantity sold is not a string"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="vest", \
            price=5000, quantity="ten"))
            self.assertEqual(response.status_code, 400)

    def test_sale_quantity_is_integer(self):
        """tests if quantity sold is an integer"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(product_name="vest", \
            price=5000, quantity=10.677))
            self.assertEqual(response.status_code, 400)

    def test_invalid_key_post_sale(self):
        """tests for invalid key when a key is missing"""
        with self.client as client:
            response = client.post("api/v1/sales", json=dict(price=5000, quantity=10))
            self.assertEqual(response.status_code, 400)

    def test_home_route(self):
        """test for the default home route"""
        with self.client as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main() 