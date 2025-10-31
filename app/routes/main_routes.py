from flask import Blueprint, request, jsonify
# from app.controllers.main_controller import get_users, create_user

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    return jsonify({"success": True, "message": "Servicio ejecutandose correctamente."})
