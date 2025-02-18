import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants  as Constants
from ...ui.routes import Route
from link_bio.components.seccion_box import seccion_box

def secciones() -> rx.Component:
    return rx.container(
        seccion_box(
            Constants.IMG_SERVICIOS,
            "handshake",
            "SERVICIOS",
            "C P K",
            "Nuestro enfoque en el gerenciamiento de neumáticos y la toma de decisiones basadas en datos, nos permiten ofrecer cómo servicio el arrendamiento de los mismos.",
            Route.SERVICIOS.value),
       rx.divider(size="4",color_scheme="mint"),   
        seccion_box(
            Constants.IMG_PRODUCTOS,
            "package-open",
            "PRODUCTOS",
            "C P K",
            "Distribuimos llantas nuevas y reencauchadas de calidad comprobada que contribuyen positivamente a incrementar la productividad de nuestros clientes.",
            Route.PRODUCTOS.value),
        rx.divider(size="4",color_scheme="mint"),   
        seccion_box(
            Constants.IMG_COMUNIDAD,
            "speech",
            "COMUNIDAD",
            "C P K",
            "Contenidos útiles en la gestión de neumáticos.",
            Route.COMUNIDAD.value),
        rx.divider(size="4",color_scheme="mint"), 
        width="100%",     
)