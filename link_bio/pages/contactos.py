
import reflex as rx

from ..views.contactos.contactos import forms_v1

import link_bio.styles.styles  as styles
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def contactos_page() -> rx.Component:
    mi_child=  rx.center(
           # header_base("/imagen/servicio5.jpg"),
            forms_v1(),
            rx.vstack(
                rx.heading("CONTACTO ", size=styles.Size.BIG.value),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin=styles.Size.BIG.value
            ),
         )
    return base_page(
       mi_child,
       hide_navbar=True
    )