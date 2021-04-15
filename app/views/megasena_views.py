from http import HTTPStatus
from flask import Blueprint,request,current_app


from flask_jwt_extended import jwt_required,get_jwt_identity


bp_megasena = Blueprint("bp_megasena", __name__, url_prefix="/megasena")

@bp_megasena.route("/sortear/<int:number>",methods=["GET"])
@jwt_required()
def draw_user(number):
    try:
        if number < 6 or number > 10:
            return {"mensagem":"dezenas (entre 6 e 10)"},HTTPStatus.BAD_REQUEST
        
        # session = current_app.db.session
        # user_id = get_jwt_identity()
        # found_user: UsersModel = UsersModel.query.get(user_id)

        # session.add(found_user)
        # session.commit()
        return {"numeros_sorteados":"TESTEE"},HTTPStatus.OK
    except Exception:
        return "Erro ao Sortear",HTTPStatus.BAD_REQUEST 