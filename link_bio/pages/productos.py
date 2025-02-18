
import reflex as rx

from ..views.header.header_base import header_base
from ..views.productos.productos import productos
from ..views.links.whatsapp import whatsapp
from ..constants  import IMG_PRODUCTOS, IMG_COMUNIDAD
import link_bio.styles.styles  as styles
import link_bio.styles.colors  as colors
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def productos_page() -> rx.Component:
    mi_child = rx.box(
        
         rx.container(
            
               rx.card(
                  header_base(IMG_PRODUCTOS),
                  
                      width="100%",
                      top= "25%", 
                        left= "50%", 
                        transform= "translate(-50%, -50%)", 
                        background_color= "rgba(0, 0, 0, 0.5)", 
                        padding="10px", 
                        border_radius= "5px" ,
                        position="absolute",
                  ),
         ), 
            rx.container(
                rx.card(                  
                          color= "white", 
                          font_size= styles.Size.DEFAULT, 
                          font_weight= "bold", 
                          padding="10px", 
                          border_radius= "15px" , 
                           
                      
                spacing="2",
                width="100%",
                
                )
            ),   
         
            rx.container(
                rx.card(
                     rx.heading(
                            "PRODUCTOS CPK", 
                            style=styles.title_style,
                            align="center"
                              
                          ), 
                    background_color= styles.Color.BACKGROUND.value,
                ),       
                        productos(IMG_COMUNIDAD,
                                "Neumáticos Reencauchados",
                                 "Llantas reencauchadas de calidad con garantía durante su vida útil."
                            ),
                        rx.divider(size="4",color_scheme="mint"),    
                        productos(IMG_COMUNIDAD,
                                "Neumáticos Nuevos",
                                 "Ofrecemos neumáticos eficientes para diferentes usos debidamente comprobados. "
                            ),
                                
                
                
        ),
            rx.container(
            whatsapp(),
            width="25%",
            ),
         )
    return base_page(
       mi_child 
    )