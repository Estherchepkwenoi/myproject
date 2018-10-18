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
    'name': 'sugar',
    'price': 2000000,
    'quantity':100
    },
    {
    'id': 2,
    'name': 'salt',
    'price': 30000000,
    'quantity':200
   },
  {
    'id': 3,
    'name': 'soap',
    'price': 4000000,
    'quantity':50
    },
]