from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app:Flask):
    db.init_app(app)
    app.db = db

    from app.models.users_model import UsersModel

    from app.models.mega_sena_model import MegaSenaModel
    