
from flask import Flask, jsonify, Blueprint,request
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
    
    @bp.route('/myproject/api/v1/products',methods=['POST'])
    def add_product():
      product = []
        'id': request.json['id'],
        'price': request.json['price'],
        'quantity':request.json['quantity'],
        'name': request.json['name']
    } 


    product=products.append(product)
    

