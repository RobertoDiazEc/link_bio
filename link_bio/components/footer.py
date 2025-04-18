import reflex as rx

from ..styles.fonts import FontSize
from ..styles.styles import title_style
from ..ui.routes import Route
from ..styles.colors import Color

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="2", font_size= FontSize.FOOTER.value,color= Color.CONTENT.value,), href=href)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "PRODUCTOS", 
            style=title_style
        ),
        footer_item("Neumáticos Reencauchados", Route.PRODUCTOS.value),
        footer_item("Neumáticos Nuevos", Route.PRODUCTOS.value),
        #footer_item("E-commerce", "/#"),
        spacing="2",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "SERVICIOS", style=title_style
        ),
        footer_item("Leasing de Neumáticos", Route.SERVICIOS.value),
        footer_item("Reembolsos", Route.SERVICIOS.value),
        #footer_item("Whitepapers", "/#"),
        spacing="2",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href, color= Color.CONTENT.value,)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.flex(
                rx.vstack(
                    
                rx.hstack(
                    rx.link(
                        rx.hstack(
                            rx.image(
                                src="/logoCPK.jpg",
                                width="4em",
                                height="auto",
                                border_radius="25%",
                                ),
                            rx.heading(
                                "", 
                                size="7", 
                                weight="bold",
                                color= Color.LINK.value
                                ),
                        ),
                        href="/"
                    ),
                   # rx.text("Otra Forma de Moverse",
                   #         size="1",
                   #         weight="bold",
                   #         color= Color.CONTENT.value),
                    align_items="center",
                ),
                rx.text(
                        "Otra Forma de Moverse  © 2024 ",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        color= Color.CONTENT.value
                    ),
                 rx.text(
                        "Email: contacto@cpkm.com.co",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        color= Color.CONTENT.value
                    ),
                    rx.text(
                        "Mobil: +57 3152 225226",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        color= Color.CONTENT.value
                    ),    
                    spacing="4",
                    align_items=[
                        "center",
                        "center",
                        "start",
                    ],
                ),
                footer_items_1(),
                footer_items_2(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.hstack(
                
                rx.hstack(
                    footer_item("Privacy Policy", Route.PRIVACYPOLICY.value),
                    footer_item("Terms of Service", "/#"),
                    footer_item("Developer: REDx Soluciones", "/#"),
                    spacing="6",
                    align="center",
                    width="100%",
                ),
                socials(),
                justify="between",
                width="100%",
            ),
            rx.divider(),
            spacing="5",
            width="100%",
        ),
        width="100%",
        bg=Color.PRIMARY.value,
    )