
import reflex as rx

from ..views.header.header_base import header_base
from ..views.despegable.opciones import opciones
import link_bio.styles.styles  as styles
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def servicios_page() -> rx.Component:
    mi_child=  rx.box(
          rx.container(
            header_base("/imagen/servicio3.jpg"),
            
            rx.box(
            rx.heading(
                   "SERVICIOS sas", 
                   size=styles.Size.BIG.value, 
                   weight="bold", 
                   as_="h6",
                   align="center",
            ),
            #position="absolute", 
            #top= "25%", 
            #left= "50%", 
            #transform= "translate(-50%, -50%)", 
            color= "white", 
            font_size= styles.Size.DEFAULT, 
            font_weight= "bold", 
            background_color= "rgba(150, 200, 200, 0.5)", 
            padding="5px", 
            border_radius= "5px" , 
            ), 
          ),
            rx.box( 
                rx.container(   
                rx.vstack(                
                    opciones(),
                    opciones(),
                    opciones(),
                    #max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin=styles.Size.BIG.value,
                    ),
                 
            ),
          padding="15px",     
         ),
    )
    return base_page(
       mi_child
    )