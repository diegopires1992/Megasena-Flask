from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class UsersModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    status = db.Column(db.String(20),nullable=False,)
    password_hash = db.Column(db.String(100), nullable=False)

    megasena_list = db.relationship('MegaSenaModel', backref='users')
    
    @property
    def password(self):
        raise TypeError("A senha não pode ser acessada")

    @password.setter
    def password(self, new_password):
        new_password_hash = generate_password_hash(new_password)
        self.password_hash = new_password_hash

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)