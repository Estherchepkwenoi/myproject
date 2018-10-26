
from flask import Flask, jsonify,request,json
from app.models.product import products, Product
from app.validations.validates import validates
import uuid

@app.route('api/v1/products',method="GET")
def get_products():
    return jsonify(products)

@app.route('api/v1/products/<id>')
def get_product(id):
    returned_product = []
    for product in products:
        for key in product:
            print(key)
            if product[key] == int(id):
                returned_product.append(product)

    return jsonify(returned_product) 
    
@app.route('api/v1/products',methods=['POST'])
def add_product(request):
    #method for adding a product into a list of products  
    try: 
        data=request.get_json()
        id=int(str(uuid.uuid4())) 
        Name = data.get_json('name')
        quantity =data.get_json('quantity')
        price = data.get_json('price') 

        valid= validates.validate_product_inputs(data['name'],data['quantity'],data['price']) 
        if valid== True:
            new_product=Product(name,quantity,price.id)
            return jsonify({"message":"product added successfully"}]),201
        else:
            return valid
