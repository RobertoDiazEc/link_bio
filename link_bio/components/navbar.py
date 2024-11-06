import reflex as rx
from datetime import datetime, timezone


class MomentState(rx.State):
    date_now: datetime = datetime.now(timezone.utc)

    def update(self):
        self.date_now = datetime.now(timezone.utc)


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
      rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "CPK", 
                        size="7", 
                        weight="bold"
                    ),
                    align_items="center",
                ),
                rx.moment(MomentState.date_now, format="YYYY-MM-DD"),
                rx.hstack(
                    navbar_link("Nosotros", "/#"),
                    navbar_link("Informacion", "/informar"),
                    navbar_link("Precios", "/#"),
                    navbar_link("Contactos", "/#"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
             ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "CPK", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("gray", 3),
        padding="1em",
        position="fixed",
        top="0px",
        z_index="1000",
        width="100%",
)   
