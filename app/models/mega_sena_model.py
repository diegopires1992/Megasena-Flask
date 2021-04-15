from . import db 


class MegaSenaModel(db.Model):
    __tablename__ = 'megasena'
    id = db.Column(db.Integer, primary_key=True)
    games_played = db.Column(db.String(100), nullable=False) 
    users_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

