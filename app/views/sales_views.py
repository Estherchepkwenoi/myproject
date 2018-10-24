from app import app
from flask import Flask, json,jsonify,request
from app.models.sales import sales, sale
from app.validations.validates import validates
import uuid

@app.route('api/v1/sales',method="GET")
def get_get():
    return jsonify(sales)

@app.route('api/v1/sales/<id>')
def get_sale(id):
    returned_sale = []
    for sale in sales:
        for key in sale:
            print(key)
            if sale[key] == int(id):
                returned_sale.append(sale)

    return jsonify(returned_sale) 
@app.route('api/v1/sales',methods=['POST'])
def add_sale(newsale):
    try:
        data=request.get_jsonify()
        name=data.get_jsonify('name')
        quantity= data.get('quantity')
        price=data.get('price')
        date= data.get('date')
        totalcost=data.get('totalcost')
        attendant=data.get('attendant')
     
        valid=validates.validate_sales(data['name'],data['quantity'],data['price'],data['date'],data['totalcost'],data['attendant'])
        if valid==True:
            newsale=sale(name,quantity,price,date,totalcost,attendant)
            return jsonify({"message":"Sale successfully Added"}),201
        else:
            return True 
    
    except:         
        response = jsonify({"message": "Invalid values"})
        response.status_code = 403
        return response      