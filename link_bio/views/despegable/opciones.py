import reflex as rx
import link_bio.styles.styles as styles

def opciones() -> rx.Component:
    return rx.card(
        rx.heading("Recoleccion de Datos",
                   style=styles.title_style),
         rx.box(
                rx.text("Nuestro personal tecnico visitara las instalaciones donde el cliente los necesite, para realizar la respectiva verificacion de los datos",
                        style=styles.title_body_style),
                rx.image(
                                src="/imagen/servicio2.jpg", 
                                width="70%", 
                                height="auto",
                                auto="format",
                            ),
             width="100%",                
            ),       
)