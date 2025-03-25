
import reflex as rx

from ..views.header.header_base import header_base_img
from ..views.despegable.opciones import opciones, opciones2
from ..constants  import IMG_SERVICIOS, IMG_LEASING2, IMG_LEASING1
from ..styles.styles import SizeTxt
import link_bio.styles.styles  as styles
import link_bio.styles.colors  as colors
from ..ui.base_page import base_page


#@rx.page(title="CPK | Servicios")
def servicios_page() -> rx.Component:
    mi_child=  rx.box(
        rx.box(
            #header_base_img(IMG_SERVICIOS),       
            rx.heading(
                "SERVICIOS C P K", 
                size=SizeTxt.BIGN1.value, 
                weight="bold", 
                as_="h6",
                align="center",
                color= styles.title_style,
            ),
            opciones2("Arrendamiento de Neumáticos CPK. ",
                             "Con una tarifa fija por kilómetro recorrido, mantenemos su vehículo con neumáticos en óptimas condiciones. ",
                             "Al registrarse podrá conocer la tarifa aplicable a su operación.",
                             IMG_LEASING2,
                    ),
             opciones("Reembolsos",
                             "Gestione el valor de los servicios emergentes a sus neumáticos.",
                             IMG_LEASING1,
                             False,
                    ),        
            width="100%", 
            background_image= f"url({IMG_SERVICIOS})",
            background_size="cover",
            background_position="center",
            background_repeat="no-repeat",
            padding="10px",           
        ),  
        
         
    )
    return base_page(
       mi_child,
       
    )