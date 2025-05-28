import reflex as rx
from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
import os


# Create a FastAPI app
api_contrato_app = FastAPI(title="API for Download Contrato")


# Add routes to the FastAPI app
@api_contrato_app.get("/api/contrato-pdf/{supplier_id}")
async def get_contrato_pdf(supplier_id: str):
    file_path = rx.get_upload_dir() / f"{supplier_id}_contrato.pdf"

    # Check if file exists
    if os.path.exists(file_path):
        return FileResponse(
            file_path,
            media_type="application/pdf",
            filename=f"{supplier_id}_contrato.pdf"
        )
    else:
        return dict(message= "Documento no encontrado en el servidor")
    



