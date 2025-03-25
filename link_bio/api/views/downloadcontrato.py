import reflex as rx
from fastapi.responses import FileResponse
import os


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
        return {"error": "Document not found"}