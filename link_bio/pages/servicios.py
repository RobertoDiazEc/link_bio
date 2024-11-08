
import reflex as rx

from link_bio.views.header.header_servicio import header_servicio
from link_bio.views.links.links import links
import link_bio.styles.styles  as styles
from .ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def servicios_page() -> rx.Component:
    return base_page(
        rx.center(
             header_servicio(),
  
            rx.vstack(
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin=styles.Size.BIG.value
            ),
         )
    )