from src.llm.load_embeddings import load
from fastapi.responses import JSONResponse
from app.schemas.chat_schema import ChatRequest
from app.utils.response import format_response


def get_info():
    return {"success": True, "message": "Chat online", "response": ""}


def post_question(req: ChatRequest):
    data = load(req.question, 1)

    status_code = data["status_code"]
    if status_code == 200 or status_code == 201:
        response = {
            "success": data["success"],
            "message": data["message"],
            "response": data["response"],
        }
    else:
        response = {
            "success": data["success"],
            "message": data["message"],
            "error": data["error"],
        }

    return JSONResponse(content=response, status_code=status_code)
