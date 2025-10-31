from fastapi import APIRouter, Depends
from app.controllers.api.chat_controller import get_info, post_question
from app.schemas.chat_schema import ChatRequest
from app.utils.security import verify_api_key

router = APIRouter()


@router.get(
    "/",
    summary="Chat",
    description="Estado del chat con los documentos PDF",
)
def root():
    return get_info()


@router.post(
    "/",
    summary="Preguntar",
    description="Preguntar a la base de conocimiento de los documentos PDF",
)
async def question(req: ChatRequest, api_key: str = Depends(verify_api_key)):
    return post_question(req)
