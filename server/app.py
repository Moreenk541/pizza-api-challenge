# server/app.py
from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so that Flask-Migrate can detect them
    from .models import pizza, restaurant, restaurant_pizza

    # Register blueprints
    from .controllers.pizza_controller import pizza_bp
    from .controllers.restaurant_controller import restaurant_bp
    from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(pizza_bp, url_prefix="/pizzas")
    app.register_blueprint(restaurant_bp, url_prefix="/restaurants")
    app.register_blueprint(restaurant_pizza_bp, url_prefix="/restaurant_pizzas")

    @app.route('/')
    def index():
        return "<h1>Pizza API</h1>"

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5003)
