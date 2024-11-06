import reflex as rx
from link_bio.components.imagen import imagen


def imagen_seccion(imagtext: str,texto1: str, texto2: str) -> rx.Component:
    return rx.vstack(
        imagen(imagtext,texto1,texto2),
       
    )
