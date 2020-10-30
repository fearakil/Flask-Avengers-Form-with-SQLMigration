from avengers_phonebook_app import app, db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique=True)
    phone = db.Column(db.String(10), nullable = False, unique=True)
    email = db.Column(db.String(100), nullable = False, unique=True)
    password = db.Column(db.String(256), nullable = False, unique=True)
    post = db.relationship('Post', backref = 'author', lazy = True)

    def __init__(self,name,phone,email,password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        """
            Grab the password that is passed into the method
            return the hashed verson of the password 
            which will be stored inside the database
        """
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return self.name, self.email

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String(30))
    phone_number = db.Column(db.String(10))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,role,phone_number,user_id):
        self.role = role
        self.phone_number = phone_number
        self.user_id = user_id

    def __repr__(self):
        return self.role, self.phone_number