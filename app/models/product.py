import uuid
class Product:
    def __init__(self, name, quantity, price, category, id= str(uuid.uuid4())):
        self.name = name
        self.quantity = quantity,
        self.price = price,
        self.id = id




products = [
    {
    'id': 1,
    'name': 'Radio',
    'price': 2000000
    },
    {
    'id': 2,
    'name': 'TV',
    'price': 30000000
}
]