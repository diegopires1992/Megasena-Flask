from http import HTTPStatus
from flask import Blueprint,request,current_app

from flask_jwt_extended import jwt_required,get_jwt_identity
from app.services.play_number_services import PlayNumber
from app.models.mega_sena_model import MegaSenaModel
from app.services.robo_services import RobotMegaSena
from app.services.data_converter import DataConvert


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

@bp_megasena.route("/atual",methods=["GET"])
@jwt_required()
def current_game():
    try:
        intancia = RobotMegaSena()
        intancia.navigate()
        resultado = intancia.get_all_number()  
        return {"sorteo_atualizado":resultado},HTTPStatus.OK
    except Exception:
        return "Erro ao executar o Robo",HTTPStatus.BAD_REQUEST

@bp_megasena.route("/acertosultimojogo",methods=["GET"])
@jwt_required()
def hit_the_last_game():
    try:
        session = current_app.db.session
        user_id = get_jwt_identity()
        intancia = RobotMegaSena()
        intancia.navigate()
        result_mega = intancia.get_all_number()

        data_mega_sena = session.query(MegaSenaModel).filter_by(users_id=user_id)

        instance = DataConvert(data_mega_sena)
        result_convert = instance.convert()

        counter = 0    
        number_correct_answers = []
        for number in result_convert:
            if number in result_mega:
                counter = counter + 1
                number_correct_answers.append(number)

        return {"numeros_de_acertos_no_ultimo_jogo":counter,"numeros_acertados":number_correct_answers},HTTPStatus.OK
    except Exception:
        return "Erro ao Sortear",HTTPStatus.BAD_REQUEST


@bp_megasena.route("/listadejogos",methods=["GET"])
@jwt_required()
def list_game():
    try:
        session = current_app.db.session
        user_id = get_jwt_identity()

        data_mega_sena = session.query(MegaSenaModel).filter_by(users_id=user_id)

        instance = DataConvert(data_mega_sena)
        result_list = instance.list_game()

        return {"lista_de_jogos":result_list},HTTPStatus.OK
    except Exception:
        return "Erro ao Sortear",HTTPStatus.BAD_REQUEST   
