from . import db

class Restaurant:
    __tablename__ ='Restaurant'

    id=db.Column(db.Integer,primaryKey=True)
    name=db.Column(db.String,nullable=False)
    address=db.Column(db.String,nullable=False)