
import reflex as rx

from ..views.contactos.contactos import contactos
import link_bio.constants as cons
from ..styles.colors import Color
from ..styles.styles import SizeTxt
import link_bio.styles.styles  as styles
from ..styles.styles import title_style
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def contactos_page() -> rx.Component:
    mi_child=  rx.flex(
        rx.center(
           # header_base("/imagen/servicio5.jpg"),
           rx.card(
                rx.heading("CONTÁCTENOS ", 
                       size=SizeTxt.BIG.value,
                       style=title_style
                       ),
                rx.box(
                         
                   rx.link(
                            rx.flex(
                                rx.icon_button("message-circle-more"),
                                rx.box(
                                    rx.heading("WHATSAPP."),
                                    rx.text(
                                        "Comunicación Directa.",
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
                    rx.text(
                        "Email: contacto@cpkm.com.co",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        color= Color.CONTENT.value
                    ),
                    rx.text(
                        "Mobil: +57 3152 225226",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        color= Color.CONTENT.value
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
    