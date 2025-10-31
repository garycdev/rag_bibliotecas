from fastapi.responses import JSONResponse


def format_response(response: dict, default_code: int = 200) -> JSONResponse:
    """
    Convierte un dict de respuesta a JSONResponse con campos estándar.
    """
    data = {
        "success": response.get("success", False),
        "message": response.get("message", "Error"),
        "response": response.get("response", None),
    }
    status_code = response.get("code", default_code)
    return JSONResponse(content=data, status_code=status_code)
