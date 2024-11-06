import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants  as Constants
from link_bio.components.seccion_web import seccion_web
from link_bio.components.seccion_webdet import seccion_webdet

def secciones() -> rx.Component:
    return rx.container(
    rx.box(
        rx.image(
                src="imagen/servicio3.jpg", 
                width="80%", 
                height="auto",
                auto="format",
        ),
       rx.box( 
        rx.vstack(
            seccion_web(
                "/imgen.jpg",
                "SERVICIOS",
                "C P K",
            ),
            seccion_webdet(
                "Contamos con materiales de primera calidad, técnicos experimentados y un enfoque centrado en el cliente para asegurarnos de que obtiene el mejor servicio para sus necesidades."
            ),
         gap="2em",
        ), 
         position="absolute", 
            top= "40%", 
            left= "50%", 
            transform= "translate(-50%, -50%)", 
            color= "white", 
            font_size= "16px", 
            font_weight= "bold", 
            background_color= "rgba(0, 0, 0, 0.5)", 
            padding="5px", 
            border_radius= "5px" , 
       ), 
    padding="2em",
    position= "relative",
    width="100%",
    ),
    rx.divider(size="4",color_scheme="red"),
    rx.box(
        rx.image(
                src="imagen/servicio4.jpg", 
                width="80%", 
                height="auto",
                auto="format",
        ),
       rx.box( 
        rx.vstack(
            seccion_web(
                "/imgen.jpg",
                "PRODUCTOS",
                "C P K",
            ),
            seccion_webdet(
                "Contamos con materiales de primera calidad, técnicos experimentados y un enfoque centrado en el cliente para asegurarnos de que obtiene el mejor servicio para sus necesidades."
            ),
         gap="2em",
        ), 
         position="absolute", 
            top= "40%", 
            left= "50%", 
            transform= "translate(-50%, -50%)", 
            color= "white", 
            font_size= "16px", 
            font_weight= "bold", 
            background_color= "rgba(0, 0, 0, 0.5)", 
            padding="5px", 
            border_radius= "5px" , 
       ), 
    padding="2em",
    position= "relative",
    width="100%",
    ),
    rx.box(
        rx.image(
                src="imagen/servicio1.jpg", 
                width="80%", 
                height="auto",
                auto="format",
        ),
       rx.box( 
        rx.vstack(
            seccion_web(
                "/imgen.jpg",
                "COMUNIDAD",
                "C P K",
            ),
            seccion_webdet(
                "Contamos con materiales de primera calidad, técnicos experimentados y un enfoque centrado en el cliente para asegurarnos de que obtiene el mejor servicio para sus necesidades."
            ),
         gap="2em",
        ), 
         position="absolute", 
            top= "40%", 
            left= "50%", 
            transform= "translate(-50%, -50%)", 
            color= "white", 
            font_size= "16px", 
            font_weight= "bold", 
            background_color= "rgba(0, 0, 0, 0.5)", 
            padding="5px", 
            border_radius= "5px" , 
       ), 
    padding="2em",
    position= "relative",
    width="100%",
    ),
)