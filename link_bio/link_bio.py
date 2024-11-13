
import reflex as rx

import link_bio.styles.styles  as styles
import link_bio.constants  as Constants
from rxconfig import config
from .ui.base_page import base_page
from .views.header.header import header
from .views.secciones.secciones import secciones
from .views.empresa.serempresa import serempresa
from .views.links.links import links
from .pages.servicios import servicios_page
from . import pages

class State(rx.State):
    """The app state."""
   
    ...

def index() -> rx.Component:
    mi_base_pag = (
        header(),
        secciones(),
        serempresa(),
        rx.vstack(
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin=styles.Size.BIG.value
            ),
        
        )
    return base_page(
        mi_base_pag        
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app.add_page(servicios_page, route="/servicios")
app.add_page(pages.productos_page, route="/productos")
app.add_page(pages.comunidad_page, route="/comunidad")
app.add_page(pages.contactos_page, route="/contactos")
app.add_page(pages.menuinterno_page, route="/menuinterno")

app._compile()