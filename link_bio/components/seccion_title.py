import reflex as rx
import link_bio.styles.styles as styles

def seccion_web(imgavatar: str, titulo: str, pie: str) -> rx.Component:
    return rx.box(
        rx.heading(titulo),
        padding= "10px",
        border=styles.Size.ZERO,
        width="100%"
    )