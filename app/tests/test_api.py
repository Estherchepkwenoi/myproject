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
            response = client.post("api/v1/products", json=dict(name="2467***",price=10000,quantity=1))
            self.assertEqual(response.status_code, 400)

    def test_product_with_empty_quantity(self):
        with self.client as client:
            response = self.client.post("/api/v1/", json=dict(name='sugar', price =2000, quantity = "",)) 
            reply = json.loads(response.data)
            self.assertEquals(reply['message'], 'Quantity is missing')
            self.assertEquals(response.status_code, 400)

    def test_product_with_empty_price(self):
        with self.client as client:
            response = self.client.post("/api/v1/", json=dict(name='sugar', price ="", quantity = "3",)) 
            reply = json.loads(response.data)
            self.assertEquals(reply['message'], 'price is missing')
            self.assertEquals(response.status_code, 400)
  
    def test_home_route(self):
         with self.client as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main() 