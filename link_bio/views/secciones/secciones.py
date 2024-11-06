import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants  as Constants
from link_bio.components.seccion_box import seccion_box

def secciones() -> rx.Component:
    return rx.container(
        seccion_box(
            "imagen/servicio3.jpg",
            "/imgen.jpg",
            "SERVICIOS",
            "C P K",
            "Contamos con materiales de primera calidad, técnicos experimentados y un enfoque centrado en el cliente para asegurarnos de que obtiene el mejor servicio para sus necesidades."
            ),
        rx.divider(size="4",color_scheme="red"),
        seccion_box(
            "imagen/servicio4.jpg",
            "/imgen.jpg",
            "PRODUCTOS",
            "C P K",
            "Contamos con materiales de primera calidad, técnicos experimentados y un enfoque centrado en el cliente para asegurarnos de que obtiene el mejor servicio para sus necesidades."
            ),
        rx.divider(size="4",color_scheme="red"),
    seccion_box(
            "imagen/servicio1.jpg",
            "/imgen.jpg",
            "COMUNIDAD",
            "C P K",
            "Contamos con materiales de primera calidad, técnicos experimentados y un enfoque centrado en el cliente para asegurarnos de que obtiene el mejor servicio para sus necesidades."
            ),
)