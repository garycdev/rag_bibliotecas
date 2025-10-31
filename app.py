# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return {
#         'success': True,
#         'message': 'Servicio ejecutandose correctamente'
#     }


# @app.route("/api/sumar", methods=["POST"])
# def sumar():
#     data = request.get_json()
#     resultado = data["a"] + data["b"]
#     return jsonify({"resultado": resultado})


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)


from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)