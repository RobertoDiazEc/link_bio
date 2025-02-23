
import reflex as rx

from ..views.header.header_base import header_base
from ..views.links.links import links
from ..constants  import IMG_COMUNIDAD
import link_bio.styles.styles  as styles
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def comunidad_page() -> rx.Component:
    mi_child = rx.box(
        rx.center(
            header_base(IMG_COMUNIDAD),
            rx.vstack(
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin=styles.Size.BIG.value
            ),
            ), 
            rx.box(
                rx.card(
                    rx.text("esto es Programas"),
                    id="card_progrmas"
                   
                ),
                rx.card(
                    rx.text("esto es videos"),
                    rx.video(
                        url="/videos/prueba1.mp4",
                        width="400px",
                        height="auto",
                    ),
                   id="card_videos"
                ),
                rx.card(
                    rx.text("esto es comunidad"),
                   id="card_comunidad"
                )
            ),
            
         )
    return base_page(
        mi_child
    )