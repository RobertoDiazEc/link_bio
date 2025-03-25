import reflex as rx

class StateImagen(rx.State):
    """El estado de la aplicación."""
    # La variable para almacenar el nombre del archivo
    video: str

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Manejar la subida de archivo(s).
        Args:
            files: Los archivos subidos.
        """
        current_file = files[0]
        upload_data = await current_file.read()
        outfile = (
            rx.get_upload_dir() / current_file.filename
        )

        # Guardar el archivo
        with outfile.open("wb") as file_object:
            file_object.write(upload_data)

        # Actualizar la variable del archivo
        self.video = current_file.filename

color = "rgb(107,99,246)"

def index():
    """La vista principal."""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Seleccionar Archivo",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                ),
                rx.text(
                    "Arrastra y suelta archivos aquí o haz clic para seleccionar"
                ),
            ),
            id="upload1",
            max_files=1,
            border=f"1px dotted {color}",
            padding="5em",
        ),
        rx.text(rx.selected_files("upload1")),
        rx.button(
            "Subir",
            on_click=StateImagen.handle_upload(
                rx.upload_files(upload_id="upload1")
            ),
        ),
        rx.button(
            "Limpiar",
            on_click=rx.clear_selected_files("upload1"),
        ),
        rx.cond(
            StateImagen.video,
            rx.video(url=rx.get_upload_url(StateImagen.video)),
        ),
        padding="5em",
    )