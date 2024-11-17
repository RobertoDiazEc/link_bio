import reflex as rx
import link_bio.constants as cons
from link_bio.components.linK_button_whatsapp import link_button_wharsaap

# Crear una función que maneje la interfaz de la aplicación
def whatsapp() -> rx.Component:
    return rx.hstack(
            link_button_wharsaap("Escribenos",
                        cons.WHATSAPP_URL,
                        "message-circle-more"),
            style={"position": "fixed",
                   "bottom": "20px", 
                   "right": "20px", 
                   "z-index": "1000"}
        )



