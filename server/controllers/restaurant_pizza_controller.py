

from flask import Blueprint, request, jsonify
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant
from ..extensions import db

restaurant_pizza_bp = Blueprint("restaurant_pizza_bp", __name__)

@restaurant_pizza_bp.route("/", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    if not (1 <= price <= 30):
        return jsonify({ "errors": ["Price must be between 1 and 30"] }), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({ "errors": ["Pizza or Restaurant not found"] }), 404

    restaurant_pizza = RestaurantPizza(
        price=price,
        pizza_id=pizza_id,
        restaurant_id=restaurant_id
    )

    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify({
        "id": restaurant_pizza.id,
        "price": restaurant_pizza.price,
        "pizza_id": pizza.id,
        "restaurant_id": restaurant.id,
        "pizza": pizza.to_dict(),
        "restaurant": restaurant.to_dict()
    }), 201
