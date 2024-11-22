
import reflex as rx

from ..views.contactos.contactos import contactos
import link_bio.constants as cons
import link_bio.styles.styles  as styles
from ..styles.styles import title_style
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def contactos_page() -> rx.Component:
    mi_child=  rx.flex(
        rx.center(
           # header_base("/imagen/servicio5.jpg"),
           rx.card(
                rx.heading("C O N T A C T O S ", 
                       size=styles.Size.BIG.value,
                       style=title_style
                       ),
                rx.box(
                   rx.link(
                            rx.flex(
                                rx.icon_button("message-circle-more"),
                                rx.box(
                                    rx.heading("WHATSAPP."),
                                    rx.text(
                                        "Comunicacion Directa.",
                                        style=styles.title_body_style,
                                    ),
                                ),
                                spacing="2",
                            ),
                            href=cons.WHATSAPP_URL,
                            cursor="pointer",
                            is_external=True,
                            width="100%",
                    ),
               
                ),
                max_width=styles.MAX_WIDTH,
                width="100%",
                variant="surface",
               ),
                
              
            rx.vstack(
                contactos(),
                width="100%",
                margin=styles.Size.DEFAULT.value 
            ),
        ),   
    )
    return base_page(
       mi_child,
       hide_navbar=False
    )
    