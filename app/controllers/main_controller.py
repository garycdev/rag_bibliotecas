from app.models.user_model import User


def get_users():
    return [user.to_dict() for user in User.sample_data()]


def create_user(data):
    return {"mensaje": f"Usuario {data.get('nombre')} creado correctamente"}
