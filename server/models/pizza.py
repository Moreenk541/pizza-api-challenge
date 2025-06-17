from config import db

class Pizza(db.Model):
    __tablename__= 'Pizza'

    id =db.Column(db.Integer,primary_Key=True)
    name=db.Column(db.String,nullable=False)
    ingredients=db.Column(db.String,nullable=False)
    

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', cascade='all, delete')
