import reflex as rx
from fastapi.responses import FileResponse
import os


async def get_placa_imagen(supplier_id: str):
    file_path = rx.get_upload_dir() / f"{supplier_id}"

    # Check if file exists
    if os.path.exists(file_path):
        return FileResponse(
            file_path,
            media_type="image/jpg" or "image/png",
            filename=f"{supplier_id}"
        )
    else:
        return {"error": "Document not found"}