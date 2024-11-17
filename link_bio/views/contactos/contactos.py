import reflex as rx

services = [
    ["Servicio", "Productos"],
    ["Flotas", "Consultoria"],
    ["Programa", "Otros"],
]


def item_and_title(title: str, placeholder: str):
    return rx.vstack(
        rx.text(title, font_size="11px", weight="medium", color_scheme="gray"),
        rx.input(placeholder=placeholder, width="100%"),
        width="100%",
        spacing="2",
    )


def check_box_item(name: str):
    return rx.box(rx.checkbox(name), width="100%")


def contactos():

    return rx.card(
        rx.vstack(
            rx.heading("Necesitas mas Informacion", size="5", weight="bold"),
            rx.text(
                "Tienes preguntas sobre nuestros productos? Nosotros estamos para ayudarte. Nuesto Equipo se comunicara lo mas rapido posible.",
                font_size="12px",
                weight="medium",
                color_scheme="gray",
                text_align="center",
            ),
            width="100%",
            spacing="4",
            align="center",
            padding="12px 12px",
        ),
        rx.hstack(
            item_and_title("Nombre Completo", "Nombre Completo"),
            width="100%",
            display="flex",
        ),
        item_and_title("Email", "example@someplace.com"),
        item_and_title("Celular", "0998765499"),
        item_and_title("Ciudad", "Ciudad"),
        rx.vstack(
            rx.text("Mensage", font_size="11px", color_scheme="gray", weight="medium"),
            rx.text_area(
                width="100%",
                placeholder="consultar ...",
                rows="5",
            ),
            width="100%",
            spacing="2",
        ),
        rx.vstack(
            rx.text("Services", font_size="11px", color_scheme="gray", weight="medium"),
            *[
                rx.hstack(
                    check_box_item(x),
                    check_box_item(y),
                    width="100%",
                )
                for x, y in services
            ],
            width="100%",
            spacing="2",
        ),
        rx.spacer(),
        rx.button(
            "Enviar",
            width="100%",
            cursor="pointer",
            variant="surface",
            color_scheme="gray",
        ),
        width="100%",
        max_width="40em",
        height="100%",
        justify="center",
        align="center",
        padding="25px 20px",
    )
