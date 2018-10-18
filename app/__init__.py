from flask import Flask, jsonify
from app.views import product_views
app = Flask(__name__)
app.register_blueprint(product_views.bp)

if __name__ == '__main__':
    app()   