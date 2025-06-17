from config import db

class Restaurant(db.Model):  # Don't forget to inherit from db.Model
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Restaurant {self.name}>"
    
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade='all, delete')
