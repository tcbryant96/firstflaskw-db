from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    address = db.relationship("Address", backref= "author", lazy= 'dynamic')
    number = db.relationship("Number", backref= "author", lazy= 'dynamic')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Save the password as the hashed version of the password
        self.set_password(kwargs['password'])
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def set_password(self,password):
        self.password = generate_password_hash(password)
        db.session.commit()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class Address(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.String(50), nullable= False)
    apartment = db.Column(db.String(50))
    city = db.Column(db.String(50), nullable= False)
    state= db.Column(db.String(50), nullable= False)
    country= db.Column(db.String(50), nullable= False)
    zip= db.Column(db.String(15), nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()  

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in ('address', 'apartment', 'city', 'state', 'country', 'zip'):
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Number(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    number= db.Column(db.String(25), nullable=False)
    provider= db.Column(db.String(50), nullable=False)
    provided_to= db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #pro = db.relationship("Provided", backref= "author", lazy= 'dynamic')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()  

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in ('number', 'provider', 'provided_to'):
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#class Provided(db.Model):
    #id = db.Column(db.Integer, primary_key= True)
    #provided_to= db.Column(db.String(50))
    #number = db.Column(db.Integer, db.ForeignKey('number.number'))

    
