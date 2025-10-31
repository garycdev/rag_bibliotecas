from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, BackgroundTasks
from app.utils.security import verify_api_key
from app.controllers.api.pdf_controller import list_documents, status_documents
from fastapi.responses import JSONResponse
from pathlib import Path
from src.llm.load_pdf import load
import shutil
import os

DATA_DIR = Path("data/documents")

router = APIRouter(
    dependencies=[Depends(verify_api_key)],
)


@router.get(
    "/",
    summary="Lista de documentos",
    description="Lista los documentos existentes para la base de conocimientos",
)
async def get_documents():
    return list_documents()


@router.get(
    "/estado",
    summary="Estado de base de conocimientos",
    description="Revisa el estado de los PDFs para la base de conocimientos",
)
async def status():
    return status_documents()


def procesar_pdf():
    print("Procesando PDF en segundo plano")
    load()
    pass


@router.post("/")
async def upload_document(
    background_tasks: BackgroundTasks, file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF")

    save_path = os.path.join("data/documents", file.filename)
    with open(save_path, "wb") as f:
        f.write(await file.read())

    background_tasks.add_task(procesar_pdf)

    return JSONResponse(
        content={
            "success": True,
            "message": "Archivo subido correctamente",
            "filename": file.filename,
        },
        status_code=201,
    )
