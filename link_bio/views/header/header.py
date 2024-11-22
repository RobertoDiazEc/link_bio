import reflex as rx
from ...components.header_button import header_button
import link_bio.styles.styles as style

def header() -> rx.Component:
    return rx.box( 
            rx.image(
                        src="imagen/arcCPK.jpg", 
                        width="100%", 
                        height="auto",
                        auto="format",
                ),
                
            rx.vstack(
                 header_button("CPK", "COSTO POR KILOMETRO"),
        
                )
            position= "relative",
            width="100%"
    )       