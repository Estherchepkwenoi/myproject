
from flask import Flask, jsonify, Blueprint,json,request
from app.models.product import products, product


bp = Blueprint('addproducts', __name__, url_prefix='/api/v1/products')

@bp.route('/myproject/api/v1/products',methods=['POST'])
def add_product():
    product = {
        'id': request.json['id'],
        'price': request.json['price'],
        'quantoty':request.json['quantoty'],
        'name': request.json['name']
    } 


    product=products.append(product)
      return jsonify({product,'message': "added successfully"}),100






