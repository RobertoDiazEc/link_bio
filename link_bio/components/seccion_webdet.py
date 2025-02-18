import reflex as rx
import link_bio.styles.styles as styles

def seccion_webdet(texto: str) -> rx.Component:
    return rx.box(
        rx.text(
            texto,
            style=styles.title_body_style,
            ),
        #position="relative", 
        font_weight= "bold",   
        border=" 1px solid green",
        padding= "5px",
        border_radius= "15px" , 
        width="80%",
)