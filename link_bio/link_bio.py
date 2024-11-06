
import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.secciones.secciones import secciones
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles  as styles
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:
    return rx.box(
         navbar(),
         header(),
         secciones(),
        rx.vstack(
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin=styles.Size.BIG.value
        ),
        footer(),
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app._compile()