import reflex as rx

from ..styles.colors import Color
from ..ui.routes import Route
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
                color= Color.CONTENT.value
                ), 
        href=url
    )

def navbar() -> rx.Component:
            
    return rx.box(
      rx.desktop_only(
            rx.hstack(
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
                        color= Color.CONTENT.value
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
               
                rx.hstack(
                    rx.badge(rx.moment(MomentState.date_now, format="YYYY-MM-DD"),color= Color.CONTENT.value,),
                    navbar_link("Servicios", Route.SERVICIOS.value),
                    navbar_link("Productos", Route.PRODUCTOS.value),
                    navbar_link("Comunidad", Route.COMUNIDAD.value),
                    navbar_link("Contactos", Route.CONTACTOS.value),
                    justify="end",
                    spacing="5",
                ),
                # rx.menu.root(
                #     rx.menu.trigger(
                #         rx.icon_button(
                #             rx.icon("user"),
                #             size="2",
                #             radius="full",
                #         )
                #     ),
                #     rx.menu.content(
                #        rx.menu.item( navbar_link( "Settings", "/#")),
                #         rx.menu.item("Earnings"),
                #         rx.menu.separator(),
                #         rx.menu.item("Log out"),
                #     ),
                #     justify="end",
                # ),
                justify="between",
                align_items="center",
             ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logoCPK.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.link(
                    rx.heading(
                        "", 
                        size="7", 
                        weight="bold"
                    ),
                    href="/"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item(navbar_link( "Servicios", Route.SERVICIOS.value)),
                        rx.menu.item(navbar_link("Productos", Route.PRODUCTOS.value)),
                        rx.menu.item(navbar_link("Comunidad", Route.COMUNIDAD.value)),
                        rx.menu.item(navbar_link("Contactos", Route.CONTACTOS.value)),
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
