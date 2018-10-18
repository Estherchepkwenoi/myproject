from flask import Flask, jsonify
from app.views import product_views
from app.views import sales_views
app = Flask(__name__)

app.register_blueprint(product_views.bp)
app.register_blueprint(sales_views.bp)


if __name__ == '__main__':
    app()   