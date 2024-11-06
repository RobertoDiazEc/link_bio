import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.serempresainfo import serempresainfo
from link_bio.components.title import title


def serempresa() -> rx.Component:
    return rx.container(
        serempresainfo(
            "Quienes Somos",
            "Los datos se han convertido en parte fundamental de nuestra vida, con ellos se toman muchas deciciones, para bien o para mal. La obtencion y la verificacion de esta informacion es fundamental y sobre todo si esto te ayuda a tus finanzas. Nosotros lo psabemos hacer.",
            "imagen/somos.jpg"
        ),
         serempresainfo(
            "Mision",
            "Los datos se han convertido en parte fundamental de nuestra vida, con ellos se toman muchas deciciones, para bien o para mal. La obtencion y la verificacion de esta informacion es fundamental y sobre todo si esto te ayuda a tus finanzas. Nosotros lo psabemos hacer.",
            "imagen/mision.jpg"
        ),
        serempresainfo(
            "Vision",
            "Los datos se han convertido en parte fundamental de nuestra vida, con ellos se toman muchas deciciones, para bien o para mal. La obtencion y la verificacion de esta informacion es fundamental y sobre todo si esto te ayuda a tus finanzas. Nosotros lo psabemos hacer.",
            "imagen/somos.jpg"
        ),
    )