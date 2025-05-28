import reflex as rx
from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
import os


# Create a FastAPI app
api_imgplaca_app = FastAPI(title="API for Download Imagen Placa")
# Add routes to the FastAPI app
@api_imgplaca_app.get("/api/placa-imagen/{supplier_id}")
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
        return dict(message= "Documento de imagen no encontrado en el servidor")