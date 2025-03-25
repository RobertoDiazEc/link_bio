"""Login page. Uses auth_layout to render UI shared with the sign up page."""

import reflex as rx

from ..backend.backend import backState
from ..state.navegar import CheckboxState
from ..ui.base_page import base_page
from ..ui.routes import Route

def login_page() -> rx.Component:
    """The login page."""
    mi_child= rx.box(
        rx.box(
            
            rx.vstack(
                rx.heading("Arrendamiento CPK ", size="8"),
                rx.heading("Inicio de sesión.", size="4"),
                align="center",
                spacing="4",
                padding="10px",
            ),
            rx.form(
                rx.flex(
                    # on_blur=AuthState.set_username,
                    #on_blur=AuthState.set_password,
                    rx.input(
                        rx.input.slot(rx.icon("user")),

                        placeholder="Username",                    
                        size="3",
                        required=True,
                        name="username",
                    ),
                            
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        type="password",
                        placeholder="Password",                        
                        size="3",
                        required=True,
                        name="password",
                    ),
                            
                    rx.hstack(
                        rx.icon("wrench"),
                        rx.link("No Recuerdas tu contraseña.", 
                            href=Route.RESETKEY.value,
                            ),
                        align="end",
                    ),
                    rx.button("Ingresar", 
                            on_click=backState.on_load, 
                            type="submit",
                            size="3", 
                            width="80%",
                    ),
                            
                    spacing="4",
                    align="center",
                    padding="10px",
                    direction="column",
                ),
                on_submit=backState.sumit_login,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.vstack(
                rx.text(
                "¿Aún no tienes cuenta? ",           
                    ),
                rx.link("Crear Cuenta aquí.", 
                        href=Route.USERCONTACTO.value,
                        on_blur=CheckboxState.on_load(False),
                    ),
                    align="center",
            ),
            align="center",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="450px",
            border_radius="8px",
        ),
        
       # padding="56px",
        border_top_radius="10px",
            box_shadow="0 4px 60px 0 rgba(0, 0, 0, 0.08), 0 4px 16px 0 rgba(0, 0, 0, 0.08)",
            display="flex",
            flex_direction="column",
            align_items="center",
            padding_top="36px",
            padding_bottom="24px",
            background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
            spacing="4",
    )
    return base_page(
       mi_child,
       True
    )