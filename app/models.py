from app import db
from datetime import datetime 



class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    data_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

   # def __init__(self, **kwargs):
     #   super().__init__(**kwargs)
      #  db.session.add(self)
       # db.session.commit()