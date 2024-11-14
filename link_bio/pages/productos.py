
import reflex as rx

from ..views.header.header_base import header_base
from ..views.links.links import links
from ..views.links.whatsapp import whatsapp
import link_bio.styles.styles  as styles
import link_bio.styles.colors  as colors
from ..ui.base_page import base_page

#@rx.page(route="pages/servicios", title="Servicios")
def productos_page() -> rx.Component:
    mi_child = rx.box(
       header_base("/imagen/servicio4.jpg"),
         rx.container(
               rx.card(
                    
                   rx.box(
                          rx.heading(
                              "PRODUCTOS CPK", 
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
                      width="100%",
                      top= "25%", 
                        left= "50%", 
                        transform= "translate(-50%, -50%)", 
                        background_color= "rgba(0, 0, 0, 0.5)", 
                        padding="10px", 
                        border_radius= "5px" ,
                        position="absolute",
                  ),
                spacing="2",
                width="100%",
                 
                
           ), 
            rx.container(
                rx.card(
                        rx.card(
                            rx.inset(
                                rx.image(
                                    src="/imagen/servicio4.jpg",
                                    width="25%",
                                    height="auto",
                                ),
                                side="top",
                                pb="current",
                            ),
                            rx.text(
                                "DESCRIPCION DEL PRODUCTO ."
                            ),
                            width="5Ovw",
                        ),
                        rx.card(
                            rx.inset(
                                rx.image(
                                    src="/imagen/servicio2.jpg",
                                    width="25%",
                                    height="auto",
                                ),
                                side="top",
                                pb="current",
                            ),
                            rx.text(
                                "DESCRIPCION DEL PRODUCTO 2."
                            ),
                            width="5Ovw",
                        ),
                rx.vstack(
                    links(),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin=styles.Size.BIG.value
                ),
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