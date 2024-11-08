
import reflex as rx

from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
import link_bio.styles.styles  as styles




def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    #print([type(x) for x in args])
        return rx.box(
        navbar(),
        child,
        rx.color_mode.button(position="bottom-left", id='mi-color-modelo-btn'),
        footer(),
        id="mi-box-base"
    )
