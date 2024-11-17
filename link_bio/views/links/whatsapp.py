import reflex as rx

from link_bio.components.linK_button_whatsapp import link_button_wharsaap

# Crear una función que maneje la interfaz de la aplicación
def whatsapp() -> rx.Component:
    return rx.hstack(
            link_button_wharsaap("Escribenos",
                        "https://wa.me/11234567890?text=Hola%20quiero%20información",
                        "message-circle-more"),
            style={"position": "fixed",
                   "bottom": "20px", 
                   "right": "20px", 
                   "z-index": "1000"}
        )



