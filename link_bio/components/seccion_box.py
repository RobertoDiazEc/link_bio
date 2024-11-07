import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants  as Constants
from link_bio.components.seccion_web import seccion_web
from link_bio.components.seccion_webdet import seccion_webdet

def seccion_box(imagen_fondo: str, iconocab: str, titulo: str, subtitulo: str, detalle: str) -> rx.Component:
    return rx.box(
        rx.image(
                src=imagen_fondo, 
                width="80%", 
                height="auto",
                auto="format",
        ),
       rx.box( 
        rx.vstack(
            seccion_web(
                iconocab,
                titulo,
                subtitulo,
            ),
            seccion_webdet(
                detalle
            ),
         gap="2em",
         
        ), 
         position="absolute", 
            top= "40%", 
            left= "50%", 
            transform= "translate(-50%, -50%)", 
            color= "white", 
            font_size= styles.Size.DEFAULT, 
            font_weight= "bold", 
            background_color= "rgba(150, 200, 200, 0.5)", 
            padding="5px", 
            border_radius= "5px" , 
       ), 
    padding="2em",
    position= "relative",
    width="100%",
)