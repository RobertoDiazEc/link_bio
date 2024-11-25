import reflex as rx
import link_bio.styles.styles as styles

def opciones(titulo: str, detalle: str, imgopcion: str) -> rx.Component:
    return rx.card(
        rx.heading(titulo,
                   style=styles.title_style),
         rx.box(
                rx.text(detalle,
                        style=styles.title_body_style),
                rx.image(
                                src=imgopcion, 
                                width="50%", 
                                height="auto",
                                margin="10px",
                            ),
             padding= "10px 10px",             
            ),       
)