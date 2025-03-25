import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.serempresainfo import serempresainfo
from ...views.empresa.empresadet import EmpresAvisoPrivacidad



def politicainfo() -> rx.Component:
    return rx.container(
        serempresainfo(
            EmpresAvisoPrivacidad.POLITICATITULO.value,
            EmpresAvisoPrivacidad.POLITICADETALLETITULO.value,
            ""
        ),
        serempresainfo(
            EmpresAvisoPrivacidad.POLITICATITULOSOMOS.value,
            EmpresAvisoPrivacidad.POLITICADETALLESOMOS.value,
            ""
        ),
        serempresainfo(
            EmpresAvisoPrivacidad.POLITICATITULORECOPILACION.value,
            EmpresAvisoPrivacidad.POLITICADETALLERECOPILACION.value,
            ""
        ),
        serempresainfo(
            EmpresAvisoPrivacidad.POLITICATITULOPORQUE.value,
            EmpresAvisoPrivacidad.POLITICADETALLEPORQUE.value,
            ""
        ),
        serempresainfo(
            EmpresAvisoPrivacidad.POLITICATITULOHACEMOS.value,
            EmpresAvisoPrivacidad.POLITICADETALLEHACEMOS.value,
            ""
        ),
        serempresainfo(
            EmpresAvisoPrivacidad.POLITICATITULOCONSERVAR.value,
            EmpresAvisoPrivacidad.POLITICADETALLECONSERVAR.value,
            ""
        ),
        serempresainfo(
            EmpresAvisoPrivacidad.POLITICATITULOINFORMACION.value,
            EmpresAvisoPrivacidad.POLITICADETALLEINFORMACION.value,
            ""
        ),
       
    )