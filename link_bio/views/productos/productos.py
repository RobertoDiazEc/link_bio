import reflex as rx
import link_bio.styles.styles as styles

def productos(proimg: str,detalle: str) -> rx.Component:
    return rx.card(
              rx.inset(
                    rx.image(
                        src=proimg,
                        width="25%",
                        height="auto",
                    ),
                side="top",
                pb="current",
                ),
                rx.text(detalle,
                        style=styles.title_body_style),
            width="5Ovw",
        )