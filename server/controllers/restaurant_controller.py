# server/controllers/restaurant_controller.py

from flask import Blueprint, jsonify
from ..models.restaurant import Restaurant
from ..extensions import db

restaurant_bp = Blueprint('restaurant_bp', __name__)

# GET /restaurants
@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200

# GET /restaurants/<id>
@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({ "error": "Restaurant not found" }), 404

    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
    }), 200

# DELETE /restaurants/<id>
@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({ "error": "Restaurant not found" }), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
