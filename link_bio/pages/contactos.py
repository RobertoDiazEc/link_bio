
import reflex as rx

from ..views.contactos.contactos import contactos

import link_bio.styles.styles  as styles
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def contactos_page() -> rx.Component:
    mi_child=  rx.center(
           # header_base("/imagen/servicio5.jpg"),
           rx.box(
                rx.heading("CONTACTO ", 
                       size=styles.Size.BIG.value,
                       
                       ),
                max_width="50em",
                height="100%",
                justify="center",
                align="center",       
           ),           
            rx.vstack(
                contactos(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin=styles.Size.BIG.value
            ),
            rx.card(
                    rx.link(
                            rx.flex(
                                rx.icon_button("message-circle-more"),
                                rx.box(
                                    rx.heading("WHATSAPP..."),
                                    rx.text(
                                        "Para una comunicacion mas directa.",
                                        style=styles.title_body_style,
                                    ),
                                ),
                                spacing="2",
                            ),
                            href="https://wa.me/11234567890?text=Hola%20quiero%20información",
                            is_external=True,
                            width="100%",
                        ),
                    as_child=True,
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    cursor="pointer",
                    variant="surface",
                    color_scheme="gray",
                    margin=styles.Size.BIG.value
                ),
         )
    return base_page(
       mi_child,
       hide_navbar=False
    )