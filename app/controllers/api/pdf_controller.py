import os
from fastapi.responses import JSONResponse
from pathlib import Path

DOCUMENTS_DIR = "data/documents"


def list_documents():
    """
    Lista únicamente los archivos PDF en data/documents/,
    devolviendo solo nombre y ruta.
    """
    if not os.path.exists(DOCUMENTS_DIR):
        os.makedirs(DOCUMENTS_DIR)

    pdf_files = []
    for nombre in os.listdir(DOCUMENTS_DIR):
        ruta_completa = os.path.join(DOCUMENTS_DIR, nombre)

        if os.path.isfile(ruta_completa) and nombre.lower().endswith(".pdf"):
            pdf_files.append(
                {"name": os.path.splitext(nombre)[0], "path": ruta_completa}
            )

    return JSONResponse(
        content={"success": True, "count": len(pdf_files), "documents": pdf_files},
        status_code=200,
    )


def status_documents():
    file_path = Path("data/embeddings/embedding_base.pkl")

    if file_path.exists():
        return JSONResponse(
            content={"success": True, "message": "Base de conocimientos actualizada."},
            status_code=200,
        )
    else:
        return JSONResponse(
            content={
                "success": False,
                "error": "Base de datos no actualizada, intentelo de nuevo mas tarde.",
            },
            status_code=401,
        )
