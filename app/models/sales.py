import uuid

class sale:
    def __init__(self,name,quantity,price,date,totalcost,attendant,id=str(uuid.uuid4())):
        self.name=name
        self.quantity=quantity,
        self.price=price,
        self.date=date
        self.totalcost=totalcost,
        self.attendant=attendant,
        self.id=id 

sales=[

    {
        'id':1,
        'name':'sugar',
        'quantity':5,
        'price':1000,
        'totalcost':5000,
        'attendant':'Esther',
        'date':21/10/2018
    },
    
    {
        'id':2,
        'name':'soap',
        'quantity':3,
        'price':4000,
        'totalcost':12000,
        'attendant':'peter',
        'date':22/10/2018
    },
     {
        'id':3,
        'name':'salt',
        'quantity':4,
        'price':3000,
        'totalcost':12000,
        'attendant':'sarah',
        'date':22/10/2018
    }
]

    