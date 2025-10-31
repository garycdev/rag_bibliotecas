import os
from fastapi import Header, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def verify_api_key(x_api_key: str = Header(None)):
    """
    Verifica la API Key y devuelve mensajes personalizados.
    """
    if x_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key faltante"
        )

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key inválida"
        )

    return x_api_key


def register_api_key_exception_handler(app: FastAPI):
    """
    Registra un manejador global para HTTPException y personaliza el JSON.
    """

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code, content={"success": False, "error": exc.detail}
        )
