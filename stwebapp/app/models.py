from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    address = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    email = db.Column(db.String(128), unique=True, index=True)
    social_media = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.name}>'

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(64))
    model = db.Column(db.String(64))
    year = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'
