from flask import Flask, jsonify
from app.views import sales_views
from app.views import product_views
app = Flask(__name__)



if __name__ == '__main__':
    app()   