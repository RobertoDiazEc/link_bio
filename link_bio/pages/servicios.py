
import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header_servicio import header_servicio
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles  as styles


@rx.page(route="pages/servicios", title="Servicios")
def servicios() -> rx.Component:
    return rx.fragment(
        rx.center(
            navbar(),
            header_servicio(),
  
            rx.vstack(
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin=styles.Size.BIG.value
            ),
            footer(),
        )
    )