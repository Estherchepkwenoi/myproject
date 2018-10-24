from flask import Flask, jsonify, Blueprint
from app.models.sales import sales, sale


bp = Blueprint('sales_views', __name__, url_prefix='/api/v1/sales')

@bp.route('/')
def get_get():
    return jsonify(sales)

@bp.route('/<id>')
def get_sale(id):
    returned_sale = []
    for sale in sales:
        for key in sale:
            print(key)
            if sale[key] == int(id):
                returned_sale.append(sale)

    return jsonify(returned_sale) 
    @bp.route('/myproject/api/v1/sales',methods=['POST'])
    def add_sale():
      sale = {
        'id': request.json['id'],
        'price': request.json['price'],
        'quantity':request.json['quantity'],
        'name': request.json['name'],
        'totalcost':request.json['totalcost'],
        'attendant':request.json['attendant'],
        
    } 
    if all(isinstance(x, str) for x in string_data) and all(isinstance(x, int) for x in int_data):
           sale = {'id':len(sales) +1, 'name':name, 'quantity':quantity, 'price':price, 'totalcost':totalcost, 'attendant':attendant,}
            sales.append(sale)
            return product, 201
        return {"message":"Enter valid values please"}, 400

    sale=sales.append(sale)