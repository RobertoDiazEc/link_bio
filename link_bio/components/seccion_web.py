import reflex as rx
import link_bio.styles.styles as styles

def seccion_web(imgavatar: str, titulo: str, pie: str) -> rx.Component:
    return rx.box(
                rx.link(
                    rx.flex(
                        rx.avatar(src=imgavatar),
                        rx.box(
                            rx.heading(titulo),
                            rx.text(pie ),
                           
                        ),
                        spacing="2",
                    ),
                ),
        as_child=True,
        padding= "1px",
        border=styles.Size.ZERO,
        width="100%"
    )
   