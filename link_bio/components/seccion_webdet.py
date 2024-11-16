import reflex as rx
import link_bio.styles.styles as styles

def seccion_webdet(texto: str) -> rx.Component:
    return rx.box(
        rx.text(
            texto,
            style=styles.title_body_style,
            ),
        border=" 1px solid green",
        width="100%",
        padding= "5px"
)