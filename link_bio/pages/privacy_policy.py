import reflex as rx

import link_bio.styles.styles  as styles
import link_bio.styles.colors  as colors
from ..styles.styles import SizeTxt
from ..views.privacidad.politica_privado import politicainfo
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def privacy_policy_page() -> rx.Component:
    mi_child = rx.box(
        rx.box(
            rx.heading(
                "Version Enero 2025", 
                size=SizeTxt.DEFAULT.value, 
                weight="bold", 
                as_="h3",
                align="center",
                color= styles.title_style, 
            ),                  
            font_size= styles.Size.DEFAULT, 
            font_weight= "bold", 
            background_color= colors.Color.SECONDARY.value, 
            padding="10px", 
            border_radius= "15px" , 
        ),
        politicainfo(),
        spacing="4",      
        width="100%", 
    )
    return base_page(
       mi_child 
    )