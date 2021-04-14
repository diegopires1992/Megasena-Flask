from http import HTTPStatus
from flask import Blueprint,request,current_app
from datetime import timedelta

from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt_identity
from app.models.users_model import UsersModel




bp_user = Blueprint("bp_user", __name__, url_prefix="/usuario")

@bp_user.route("/cadastro",methods=["POST"])
def create_user():
    try:
        session = current_app.db.session
        
        body = request.get_json()
        if not body:
            return {"msg": "Verifique o body da requisição"},HTTPStatus.BAD_REQUEST

        name = body.get("name")
        email = body.get("email")
        password = body.get("password")

        new_user = UsersModel(name=name,email=email)
        new_user.password = password
        session.add(new_user)
        session.commit()

        access_token = create_access_token(identity=new_user.id,expires_delta=timedelta(days=7))
        fresh_token = create_access_token(identity=new_user.id,expires_delta=timedelta(days=14))
        return {
                "user":{
                    "name":new_user.name,
                    "email":new_user.email,
                    "access_token":access_token,
                    "fresh_token":fresh_token
                    }
                },HTTPStatus.CREATED

    except KeyError:
        return {"msg": "Verifique o body da requisição"},HTTPStatus.BAD_REQUEST
    
@bp_user.route("/login",methods=['POST'])
def login():
    body = request.get_json()
    email = body.get('email')
    password = body.get('password')

    found_user: UsersModel = UsersModel.query.filter_by(email=email).first()

    if not found_user or not found_user.check_password(password):
        return {"msg": "Usuario ou senha incorreto"},HTTPStatus.BAD_REQUEST

    access_token = create_access_token(identity=found_user.id,expires_delta=timedelta(days=7))
    fresh_token = create_access_token(identity=found_user.id,expires_delta=timedelta(days=14))

    return{"access_token":access_token,"fresh_token":fresh_token}

