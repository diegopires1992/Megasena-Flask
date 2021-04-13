from . import db

class UsersModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    password= db.Column(db.String(100), nullable=False)
    
