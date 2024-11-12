
import reflex as rx

from ..views.header.header_base import header_base
from ..views.links.links import links
from ..views.links.whatsapp import whatsapp
import link_bio.styles.styles  as styles
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def productos_page() -> rx.Component:
    mi_child = rx.box(
        rx.container(
            rx.card(
                header_base("/imagen/servicio4.jpg"),
                rx.vstack(
                    links(),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin=styles.Size.BIG.value
                ),
                ),
        ),
            rx.container(
            whatsapp(),
            width="25%",
            ),
         )
    return base_page(
       mi_child 
    )