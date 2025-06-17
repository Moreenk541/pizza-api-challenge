from config import db

class RestaurantPizza(db.Model):
    __tablename__ ='RestaurantPizza'

    id = db.column(db.Integer,primary_Key=True)
    price = db.column(db.Integer,range(1-30))

  



