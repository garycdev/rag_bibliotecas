from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from app.routes.api import api_routes, chat_routes, pdf_routes
# from app.routers.admin import dashboard, users as admin_users
from app.utils.security import register_api_key_exception_handler

app = FastAPI(title="Servicio RAG")

register_api_key_exception_handler(app)

# app.mount("/static", StaticFiles(directory="app/static"), name="static")
# templates = Jinja2Templates(directory="app/templates")

app.include_router(api_routes.router, prefix="/api", tags=["inicio"])
app.include_router(chat_routes.router, prefix="/api/chat", tags=["chat"])
app.include_router(pdf_routes.router, prefix="/api/documentos", tags=["docs"])