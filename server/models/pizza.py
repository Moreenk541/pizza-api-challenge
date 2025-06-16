from . import db

class pizza:
    __tablename__= 'pizza'

    id =db.Column(db.Integer,primaryKey=True)
    name=db.Column(db.String,nullable=False)
    ingredients=db.Column(db.string,nullable=False)
    
    pass