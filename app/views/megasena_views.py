from http import HTTPStatus
from flask import Blueprint,request,current_app

from flask_jwt_extended import jwt_required,get_jwt_identity
from app.services.play_number_services import PlayNumber
from app.models.mega_sena_model import MegaSenaModel


bp_megasena = Blueprint("bp_megasena", __name__, url_prefix="/megasena")

@bp_megasena.route("/sortear/<int:number>",methods=["GET"])
@jwt_required()
def plays_user(number):
    try:
        if number < 6 or number > 10:
            return {"mensagem":"dezenas (entre 6 e 10)"},HTTPStatus.BAD_REQUEST        

        session = current_app.db.session
        user_id = get_jwt_identity()
        instance = PlayNumber(number)
        draw_number = instance.numbers()
        new_game = MegaSenaModel(games_played=draw_number,users_id=user_id)
        session.add(new_game)
        session.commit()
        return {"numeros_sorteados":draw_number},HTTPStatus.OK
    except Exception:
        return "Erro ao Sortear",HTTPStatus.BAD_REQUEST

@bp_megasena.route("/sortear/<int:number>",methods=["GET"])
@jwt_required()
def plays_user(number):
    try:
        if number < 6 or number > 10:
            return {"mensagem":"dezenas (entre 6 e 10)"},HTTPStatus.BAD_REQUEST        

        session = current_app.db.session
        user_id = get_jwt_identity()
        instance = PlayNumber(number)
        draw_number = instance.numbers()
        new_game = MegaSenaModel(games_played=draw_number,users_id=user_id)
        session.add(new_game)
        session.commit()
        return {"numeros_sorteados":draw_number},HTTPStatus.OK
    except Exception:
        return "Erro ao Sortear",HTTPStatus.BAD_REQUEST  
