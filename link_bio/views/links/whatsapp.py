import reflex as rx

from link_bio.components.link_button import link_button

# Crear una función que maneje la interfaz de la aplicación
def whatsapp() -> rx.Component:
    return rx.card(
        rx.hstack(
            link_button("Enviar mensaje",
                        "https://wa.me/11234567890?text=Hola%20quiero%20información",
                        "message-circle-more")
             
            ),
        )



