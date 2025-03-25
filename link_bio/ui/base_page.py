
import reflex as rx

from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from ..ui.cookie import alert_dialog2, LocalStorageState


import link_bio.styles.styles  as styles




def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    #print([type(x) for x in args])

        if hide_navbar:
                return rx.box(
                
                child,
                rx.color_mode.button(position="bottom-left", id='mi-color-modelo-btn'),
                #footer(),
                id="mi-box-baseTrue",
                background_image= f"url(/imagen/servicio3.jpg)",
                #position="absolute",
                #display="flex",
                width="100%",
                border_radius="15px",
                box_shadow="0 25px 50px rgba(0, 0, 0, 0.3)",
                background_size="cover",    #/"cover","contain"
                background_position="center",
                #background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
                *args, **kwargs
            )
        else:
            return rx.box(
                navbar(),   
                child,
                rx.color_mode.button(position="bottom-left", id='mi-color-modelo-btn'),
                footer(),
                rx.cond(
                    LocalStorageState.botoncookie,
                    alert_dialog2(LocalStorageState.on_load()),
                ),
                id="mi-box-base",
                *args, **kwargs
            )    
