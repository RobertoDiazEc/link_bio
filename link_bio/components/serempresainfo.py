import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants  as Constants
from link_bio.components.title import title


def serempresainfo(titulo: str, detalle: str, imginfo: str) -> rx.Component:
    return rx.box(
           title(titulo),
            rx.text(
                detalle,
                style=styles.button_title_style),
             rx.image(
                src=imginfo, 
                width="100%", 
                height="auto",
                auto="format",
                ),    
            ppadding= "10px",
            border=styles.Size.ZERO,
            width="100%"
        )
        
