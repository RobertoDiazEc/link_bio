import reflex as rx

from ..styles.colors import Color
from datetime import datetime, timezone


class MomentState(rx.State):
    date_now: datetime = datetime.now(timezone.utc)

    def update(self):
        self.date_now = datetime.now(timezone.utc)


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, 
                size="4", 
                weight="medium", 
                color= "teal"
                ), 
        href=url
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
                    rx.link(
                    rx.heading(
                        "C P K", 
                        size="7", 
                        weight="bold"
                    ),
                    href="/"
                    ),
                    align_items="center",
                ),
               
                rx.hstack(
                    rx.badge(rx.moment(MomentState.date_now, format="YYYY-MM-DD")),
                    navbar_link("Servicios", "/servicios"),
                    navbar_link("Productos", "/productos"),
                    navbar_link("Comunidad", "/comunidad"),
                    navbar_link("Contactos", "/contactos"),
                    justify="end",
                    spacing="5",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                       rx.menu.item( navbar_link( "Settings", "/menuinterno")),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
                    justify="end",
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
        #display= "flex",
        bg=Color.PRIMARY.value,
        #background_color=cambionavbar.colorbase,
        padding="1em",
        position="fixed",
        top="0px",
        z_index="1000",
        width="100%",
        overflow="auto"  
       
)   
