from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata=MetaData()

db=SQLAlchemy(metadata=metadata)



from .pizza import pizza
from .restaurant import restaurant
from .restaurant_pizza import restaurant_pizza