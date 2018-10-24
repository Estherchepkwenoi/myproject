from flask import jsonify
from app.models.product import products, product
from app.models.sales import sales, sale 

products=[]
sales=[]
 
class validate():
# method to validate product inputs

 def validate_product_inputs(self,name,quantity,price,category):
     if name =='':
        return jsonify({"message":"The name is missing"}), 400
     elif '' in name:
        return jsonify({"message":"The name can't be empty"}), 400
    elif quantity =='':
        return jsonify({"message":"Quantity should not have spaces"}),400
    elif price =='':
        return jsonify({"message":"Price cannot be empty"}),400 
    elif category =='':
        return jsonify({"message":"category cannot be empty"}),400         