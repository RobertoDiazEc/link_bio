import reflex as rx
from link_bio.views.header.button_header import button_header
import link_bio.styles.styles as style

def header() -> rx.Component:
    return rx.box( 
                rx.image(
                        src="imagen/arcCPK.jpg", 
                        width="100%", 
                        height="auto",
                        auto="format",
                ),
                
            button_header(),
            position= "relative",

            # 
            width="100%"
    )       