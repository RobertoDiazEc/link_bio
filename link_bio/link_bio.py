
import reflex as rx


import link_bio.styles.styles  as styles
import link_bio.constants  as Constants
from rxconfig import config

from .ui.base_page import base_page
from .ui.routes import Route
from .views.header.header_base import header_base
from .views.secciones.secciones import secciones
from .views.empresa.serempresa import serempresa
from .views.links.links import links
from .state.base import baseState
from . import pages, leasing





def index() -> rx.Component:
    mi_base_pag = (
       
        header_base(Constants.CPK_LOGO),
        secciones(),
        serempresa(),
        rx.vstack(
            #links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin=styles.Size.BIG.value
            ),
       
        )
    return base_page(
        mi_base_pag,
        hide_navbar=False     
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
     theme=rx.theme(
        appearance="light", 
        has_background=True, 
        radius="large", 
        accent_color="lime"
    )

)

title = "CPK | Costo por Kilometro"
description = ""
preview = Constants.CPK_LOGO

app.add_page(index,
             title=title,
             description=description,
             image=preview,
             )

app.add_page(pages.servicios_page, title="CPK | Servicios", route=Route.SERVICIOS.value)
app.add_page(pages.productos_page, title="CPK | Productos", route=Route.PRODUCTOS.value)
app.add_page(pages.comunidad_page, title="CPK | Comunidad", route=Route.COMUNIDAD.value)
app.add_page(pages.contactos_page, title="CPK | Contactos", route=Route.CONTACTOS.value)
app.add_page(pages.menuinterno_page, title="CPK | Servicios", route="/menuinterno")
app.add_page(leasing.leasing_page, title="CPK | Leasing", route=Route.LEASING.value, on_load= baseState.check_login())
app.add_page(leasing.login_page, title="CPK Registro", route=Route.LOGINCPK.value)
app.add_page(leasing.signup_page, title="CPK Usuarios", route=Route.USERCONTACTO.value)




