
import reflex as rx

from ..views.header.header_base import header_base
from ..views.productos.productos import productos
from ..views.links.whatsapp import whatsapp
from ..constants  import IMG_PRODUCTOS
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
                        productos("/imagen/servicio2.jpg",
                                "DESCRIPCION DEL PRODUCTO 1. mirando el futuro"
                            ),
                        productos("/imagen/servicio2.jpg",
                                "DESCRIPCION DEL PRODUCTO 2. mirando el futuro"
                            ),
                         productos("/imagen/servicio2.jpg",
                                "DESCRIPCION DEL PRODUCTO 3. mirando el futuro"
                            ),
                         productos("/imagen/servicio2.jpg",
                                "DESCRIPCION DEL PRODUCTO 4. mirando el futuro"
                            ),
                         productos("/imagen/servicio2.jpg",
                                "DESCRIPCION DEL PRODUCTO 5. mirando el futuro"
                            ),         
                
                background_color= styles.Color.SECONDARY.value,
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