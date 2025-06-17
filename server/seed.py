from .app import create_app, db
from .models.pizza import Pizza
from .models.restaurant import Restaurant
from .models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Cheese, Pepperoni")

    r1 = Restaurant(name="Mama's Pizza", address="123 Flavor Street")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Cheesy Blvd")

    db.session.add_all([p1, p2, r1, r2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=15, restaurant_id=r2.id, pizza_id=p1.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()
