import reflex as rx
import link_bio.styles.styles as styles
from ..styles.styles import Size
from ..styles.styles import SizeTxt
import link_bio.constants  as Constants

from .index_imagen import imageninfo
from ..views.empresa.empresadet import Empresadetvalores
from ..views.empresa.empresadet import Empresadetobjetivos


def serempresainfo(titulo: str, detalle: str, imginfo: str) -> rx.Component:
    return rx.box(
           rx.heading(titulo,
                size=SizeTxt.BIG.value,
                style=styles.title_style,
                ),
           rx.text(
                detalle,
                style=styles.title_body_style),
            imageninfo(imginfo),
            rx.divider(),            
            padding=Size.MEDIUM.value,
            border=styles.Size.ZERO,
            width="100%"
        )

def serempresainfolista(titulo: str, detalle: str) -> rx.Component:
    return rx.box(
           rx.heading(titulo,
                size=SizeTxt.BIG.value,
                style=styles.title_style,
                ),
           rx.text(
                detalle,
                style=styles.title_body_style),
            rx.divider(),            
            padding=Size.MEDIUM.value,
            border=styles.Size.ZERO,
            width="100%"
        )


def serempresaValores(titulop: str, imginfop: str) -> rx.Component:
    return rx.box(
        rx.heading(titulop,
                size=SizeTxt.BIG.value,
                style=styles.title_style
                ),
        rx.list.unordered(
            rx.list.item(Empresadetvalores.CREATIVIDAD.value),
            rx.list.item(Empresadetvalores.CUMPLIMIENTO.value),
            rx.list.item(Empresadetvalores.INTEGRIDAD.value),
            style=styles.title_body_style
            ),
        imageninfo(imginfop),
        rx.divider(),           
        ppadding= "10px",
        border=styles.Size.ZERO,
        width="100%"    
)

def serempresaObjetivos(tituloo: str, imginfoo: str) -> rx.Component:
    return rx.box(
        rx.heading(tituloo,
                size=SizeTxt.BIG.value,
                style=styles.title_style
                ),
        rx.list.unordered(
            rx.list.item(Empresadetobjetivos.OBJETIVO1.value),
            rx.list.item(Empresadetobjetivos.OBJETIVO2.value),
            rx.list.item(Empresadetobjetivos.OBJETIVO3.value),
            rx.list.item(Empresadetobjetivos.OBJETIVO4.value),
            rx.list.item(Empresadetobjetivos.OBJETIVO5.value),
            style=styles.title_body_style
            ),
        imageninfo(imginfoo),
        rx.divider(),  
        ppadding= "10px",
        border=styles.Size.ZERO,
        width="100%"    
)
