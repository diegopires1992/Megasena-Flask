from flask import Blueprint,request,current_app
from http import HTTPStatus

from flask.globals import session
from app.models.users_model import UsersModel

bp_user = Blueprint("bp_user", __name__, url_prefix="/user")

@bp_user.route('user',methods=["POST"])
def create_user():
    session = current_app.db.session
    data = request.get_json()
    user = UsersModel(name=data["name"],password=data["password"])
    session.add(user)
    session.commit()
    return "",HTTPStatus.CREATED