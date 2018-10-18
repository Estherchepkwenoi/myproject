
from flask import Flask, jsonify, Blueprint
from app.models.product import products, Product

bp = Blueprint('products_views', __name__, url_prefix='/api/v1/products')

@bp.route('/')
def get_products():
    return jsonify(products)

@bp.route('/<id>')
def get_product(id):
    returned_product = []
    for product in products:
        for key in product:
            print(key)
            if product[key] == int(id):
                returned_product.append(product)

    return jsonify(returned_product) 
@bp.route('/')     
def add_product():
    

