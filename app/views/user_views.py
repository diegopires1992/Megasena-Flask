from http import HTTPStatus
from flask import Blueprint,request,current_app
from datetime import timedelta

from flask.globals import session

from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt_identity
from app.models.users_model import UsersModel




bp_user = Blueprint("bp_user", __name__, url_prefix="/usuario")

@bp_user.route("/cadastro",methods=["POST"])
def create_user():
    try:
        session = current_app.db.session
        
        body = request.get_json()

        name = body.get("name")
        email = body.get("email")
        password = body.get("password")

        found_user: UsersModel = UsersModel.query.filter_by(email=email).first()
        if found_user:
            return {"msg": "Usuario já cadastrado"},HTTPStatus.BAD_REQUEST

        if not body:
            return {"msg": "Verifique o body da requisição"},HTTPStatus.BAD_REQUEST

        new_user = UsersModel(name=name,email=email)
        new_user.password = password
        session.add(new_user)
        session.commit()

        access_token = create_access_token(identity=new_user.id,expires_delta=timedelta(days=7))
        return {
                "user":{
                    "name":new_user.name,
                    "email":new_user.email,
                    "access_token":access_token
                    }
                },HTTPStatus.CREATED

    except Exception:
        return {"msg": "Erro ao cadastrar"},HTTPStatus.BAD_REQUEST
    
@bp_user.route("/login",methods=['POST'])
def login():
    try:
        body = request.get_json()
        email = body.get('email')
        password = body.get('password')

        found_user: UsersModel = UsersModel.query.filter_by(email=email).first()

        if not found_user or not found_user.check_password(password):
            return {"msg": "Usuario ou senha incorreto"},HTTPStatus.BAD_REQUEST

        access_token = create_access_token(identity=found_user.id,expires_delta=timedelta(days=7))

        return{"access_token":access_token}
    except Exception:
        return {"msg": "Erro ao fazer login"},HTTPStatus.BAD_REQUEST

@bp_user.route("/",methods=["PUT"])
@jwt_required()
def update_user():
    try:
        session = current_app.db.session
        body = request.get_json()
        user_id = get_jwt_identity()

        body = request.get_json()
        if not body:
            return {"msg": "Verifique o body da requisição"},HTTPStatus.BAD_REQUEST
            
        name = body.get("name")
        email = body.get("email")
        password = body.get("password")

        found_user: UsersModel = UsersModel.query.get(user_id)
        found_user.name = name
        found_user.email = email
        found_user.password = password

        session.add(found_user)
        session.commit()

        return{
            "user":{
                "name":found_user.name,
                "email":found_user.email
            }
        },HTTPStatus.OK

    except Exception:
        return {"msg": "Erro ao fazer update no usuario"},HTTPStatus.BAD_REQUEST

