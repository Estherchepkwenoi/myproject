
from flask import Flask, jsonify, Blueprint,json,request
from app.models.addproducts import products, product


bp = Blueprint('products', __name__, url_prefix='/api/v1/products')

@bp.route('/myproject/api/v1/products',methods=['POST'])
def add_product():
    product = {
        'id': request.json['id'],
        'price': request.json['price'],
        'quantity':request.json['quantity'],
        'name': request.json['name']
    } 


    product=products.append(product)
     






