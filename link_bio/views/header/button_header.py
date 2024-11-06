import reflex as rx
from link_bio.components.header_button import header_button
import link_bio.constants  as Constants

def button_header() -> rx.Component:
    return rx.vstack(
        header_button("CPK", "COSTO POR KILOMETRO"),
        
    )
