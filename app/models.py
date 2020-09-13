from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, url_for
from sqlalchemy.orm import validates
from flask_login import UserMixin
from . import login_manager
from . import db


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8 
    ADMIN = 16

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15),unique=True)
    email = db.Column(db.String(15),unique=True)
    password = db.Column(db.String(80))    
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username) 
        
    def set_password(self, password):
        if not password:
            raise AssertionError('Password not provided')
        
        if len(password) < 8 or len(password) > 50:
            raise AssertionError('Password must be between 8 and 50 characters')
        
        self.password_hash = generate_password_hash(password) 
        
    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)

    def ping(self):
        self.last_seen = datetime.utcnow()

    @validates('username') 
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
            
        if User.query.filter(User.username == username).first():
            raise AssertionError('Username is already in use')
            
        if len(username) < 5 or len(username) > 20:
            raise AssertionError('Username must be between 5 and 20 characters') 
            
        return username 
        
    @validates('email')     
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        return email