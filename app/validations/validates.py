from flask import jsonify
from app.views.products import products 
from app.models.sales import sales, sale 

products=[]
sales=[]
 
class validate():
# method to validate product inputs

 def validate_product_inputs(self,name,quantity,price,category,id):
     if name =='':
        return jsonify({"message":"The name is missing"}), 400
     elif '' in name:
        return jsonify({"message":"The name can't be empty"}), 400
     elif quantity == '':
        return jsonify({"message":"Quantity should not have spaces"}),400
     elif price =='':
        return jsonify({"message":"Price cannot be empty"}),400 
     elif category =='':
        return jsonify({"message":"category cannot be empty"}),400 
     elif id=='':
        return jsonify({"message":"id cant be empty"}),400
     elif len(id)<0:
        return jsonify({"message":"id length cannot be less than zero"})    
     else:
        return True  

    # method for validating the sales inputs

 def validate_sales(self,name,quantity,price,date,totalcost,attendant,id):
     if name =='':
        return jsonify({"message":"The name is missing"}), 400
     elif quantity == '':
        return jsonify({"message":"Quantity should not have spaces"}),400
     elif price =='':
        return jsonify({"message":"Price cannot be empty"}),400 
     elif price =='':
        return jsonify({"message":"price cannot be empty"}),400 
     elif id=='':
        return jsonify({"message":"id cannot be empty"}),400
     elif date=='':
        return jsonify({"message":"date  cannot be empty"}),400
     elif totalcost=='':
        return jsonify({"message":"totalcost  cannot be empty"}),400
     elif attendant=='':
        return jsonify({"message":"attendant cannot be empty"}),400      
     else:
        return True 


           