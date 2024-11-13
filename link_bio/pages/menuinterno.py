import reflex as rx

from ..views.despegable.menuestatico import menuestatico
import link_bio.styles.styles  as styles
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def menuinterno_page() -> rx.Component:
    mi_child = rx.center(
           menuestatico()
         )
    return base_page(
        mi_child
    )