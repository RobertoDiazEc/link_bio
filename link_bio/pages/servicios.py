
import reflex as rx

from ..views.header.header_base import header_base
from ..views.despegable.opciones import opciones
import link_bio.styles.styles  as styles
import link_bio.styles.colors  as colors
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def servicios_page() -> rx.Component:
    mi_child=  rx.box(
        header_base("/imagen/servicio3.jpg"),
         rx.card(
                      
                      rx.box(
                          rx.heading(
                              "SERVICIOS CPK", 
                              size=styles.Size.BIGN1.value, 
                              weight="bold", 
                              as_="h6",
                              align="center",
                              color= styles.title_style, 
                          ),                  
                          font_size= styles.Size.DEFAULT, 
                          font_weight= "bold", 
                          background_color= colors.Color.SECONDARY.value, 
                          padding="10px", 
                          border_radius= "15px" , 
                      ),
                 
                spacing="4",
                width="100%",
           ), 
            rx.card( 
                rx.flex(                
                    opciones("Leasing de Neumáticos",
                             "Con una tarifa fija por kilómetro recorrido, mantenemos su vehículo con neumáticos en óptimas condiciones.",
                             "/imagen/leasing2.jpg"),
                    opciones("Reembolsos",
                             "Gestione el valor de los servicios emergentes a sus neumáticos.",
                             "/imagen/leasing1.jpg"),
                    
                    #max_width=styles.MAX_WIDTH,
                    margin=styles.Size.DEFAULT.value,
                    direction="column",
                    spacing="4",
                    flex_wrap="wrap",
                    width="100%",
                    #height="100vh",
                    margin_top="16px",
                    padding="15px",
                    ),
              spacing="4",      
              width="100%",     
            #padding="15px", 
            #margin_bottom="0.2",  
    
           
         ),
         
    )
    return base_page(
       mi_child
    )