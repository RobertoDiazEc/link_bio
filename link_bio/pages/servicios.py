
import reflex as rx

from ..views.header.header_base import header_base
from ..views.despegable.opciones import opciones
import link_bio.styles.styles  as styles
import link_bio.styles.colors  as colors
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def servicios_page() -> rx.Component:
    mi_child=  rx.box(
         rx.container(
             
                  rx.card(
                      header_base("/imagen/servicio3.jpg"),
                      rx.box(
                          rx.heading(
                              "SERVICIOS CPK", 
                              size=styles.Size.BIGN1.value, 
                              weight="bold", 
                              as_="h6",
                              align="center",
                          ),                  
                          color= "white", 
                          font_size= styles.Size.DEFAULT, 
                          font_weight= "bold", 
                          background_color= colors.Color.PRIMARY.value, 
                          padding="10px", 
                          border_radius= "15px" , 
                      ),
                  ),
                spacing="2",
                width="100%",
        
              #
              padding="15px",  
            #  background_color= colors.Color.SECONDARY.value,
              margin_bottom="0.2", 
  
         ), 
            rx.box( 
                rx.container(   
                rx.flex(                
                    opciones(),
                    opciones(),
                    opciones(),
                    #max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin=styles.Size.BIG.value,
                    direction="column",
                    spacing="2",
                    ),
                 
            padding="15px", 
            margin_bottom="0.2",  
            ),
             
         ),
    )
    return base_page(
       mi_child
    )