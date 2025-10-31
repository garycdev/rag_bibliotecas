from flask import Blueprint, request, jsonify

from app.controllers.chat_controller import get_info, post_message

chat = Blueprint("chat", __name__)


@chat.route("/", methods=["GET"])
def index():
    return get_info()

@chat.route("/", methods=["POST"])
def question():
    data = request.get_form()
    return jsonify(data)