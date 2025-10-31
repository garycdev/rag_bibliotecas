from fastapi import APIRouter
from app.controllers.api.api_controller import get_info

router = APIRouter()


@router.get(
    "/",
    summary="Inicio",
    description="Muestra el estado de funcionamiento de la API",
)
def root():
    return get_info()
