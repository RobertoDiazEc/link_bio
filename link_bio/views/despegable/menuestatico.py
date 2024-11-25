import reflex as rx

class Content(rx.State):
    links: list[dict[str, str]] = [
        {"label": "Usuarios", "link": "#usage", "color": "gray"},
        {"label": "Seguimiento", "link": "#position", "color": "gray"},
        {"label": "Productos", "link": "#overlays", "color": "gray"},
        {"label": "Graficas", "link": "#focus", "color": "gray"},
        {"label": "Ejemplos", "link": "#1", "color": "gray"},
        {"label": "Empresas", "link": "#2", "color": "gray"},
        {"label": "Recursos", "link": "#3", "color": "gray"},
        {"label": "Salir", "link": "#4", "color": "gray"},
    ]

    index: int = 0
    position_y: str = "20px"

    async def toggle_table_content(self, index: int, item: dict[str, str]):
        self.links = [
            (
                {**data, "color": rx.color("slate", 11)}
                if data["label"] != item["label"]
                else {**data, "color": rx.color("slate", 12)}
            )
            for data in self.links
        ]
        self.position_y = f"{10 + (index * 30)}px"


def items(index: int, data: dict[str, str]):
    return rx.hstack(
        rx.link(
            rx.text(
                data["label"],
                font_size="14px",
                color=data["color"],
                weight="medium",
                on_click=Content.toggle_table_content(index, data),
            ),
            href=data["link"],
            text_decoration="none",
        ),
        border_left=f"1px solid {rx.color('gray', 5)}",
        width="200px",
        height="30px",
        align="center",
        justify="start",
        padding_left="15px",
        border_radius="0px 5px 5px 0px",
    )


def item_header():
    return rx.hstack(
        rx.text("Menu Items", font_size="24px", color_scheme="gray", weight="medium"),
        rx.icon(tag="puzzle", size=12),
        width="100%",
        justify="between",
        align="center",
        border_left=f"1px solid {rx.color('gray', 5)}",
        border_radius="0px 5px 5px 0px",
        padding_left="15px",
        padding_right="15px",
        height="30px",
        bg=rx.color("gray", 3),
    )


def menuestatico():
    return rx.box(
        rx.container(
            rx.box(
            rx.card( item_header(),
                    padding="35px",
                    ),
             width="80px",
                height="80px",
                border_radius="10px",
                ),       
            rx.card(
rx.vstack(
       
        rx.vstack(
            rx.box(
                width="10px",
                height="10px",
                border_radius="10px",
                bg=rx.color("blue"),
                position="absolute",
                left="-4.5px",
                top=Content.position_y,
                transition="all 200ms ease-out",
            ),
            rx.foreach(
                Content.links,
                lambda data, index: items(index, data),
            ),
            spacing="0",
            position="relative",
        ),
        spacing="0",
    )
        )
        )
    )
