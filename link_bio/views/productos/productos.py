import reflex as rx


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
                rx.text(detalle),
            width="5Ovw",
        )