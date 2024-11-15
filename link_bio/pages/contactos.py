
import reflex as rx

from ..views.header.header_base import header_base
from ..views.links.links import links
from ..components.menualterno import sidebar
import link_bio.styles.styles  as styles
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def contactos_page() -> rx.Component:
    mi_child=  rx.center(
           # header_base("/imagen/servicio5.jpg"),
            #sidebar(),
            rx.vstack(
                rx.heading("CONTACTO ", size=styles.Size.BIG.value),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin=styles.Size.BIG.value
            ),
         )
    return base_page(
       mi_child
    )