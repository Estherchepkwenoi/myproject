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