from flask import Flask, jsonify, Blueprint,json,request
from app.models.sales import sales, sale
from datetime import datetime 


bp = Blueprint('sales', __name__, url_prefix='/api/v1/sales')

@bp.route('/myproject/api/v1/sales',methods=['POST'])
def add_sale():
    sale = {
        'id': request.json['id'],
        'price': request.json['price'],
        'quantity':request.json['quantity'],
        'name': request.json['name'],
        'totalcost':request.json['totalcost'],
        'attendant':request.json['attendant'],
        'date':datetime.datetime.utcnow()
    } 


    sale=sales.append(sale)
              