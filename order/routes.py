from flask import Blueprint, jsonify, request
import requests


order_blueprint = Blueprint('order_api_routes', __name__, url_prefix="/api/order")

USER_API_URL = 'http://127.0.0.1:5001/api/user'


@order_blueprint.route('/', methods=['GET'])
def get_open_order():
    return "Open order"


@order_blueprint.route('/all', methods=['GET'])
def all_orders():
   return "All orders"


@order_blueprint.route('/add-item', methods=['POST'])
def add_order_item():
    return "Add order item"


@order_blueprint.route('/checkout', methods=['POST'])
def checkout():
    return "Checkout"