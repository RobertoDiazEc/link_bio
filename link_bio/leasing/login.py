"""Login page. Uses auth_layout to render UI shared with the sign up page."""

import reflex as rx
from ..state.auth import AuthState
from ..ui.base_page import base_page
from ..ui.routes import Route

def login_page() -> rx.Component:
    """The login page."""
    mi_child= rx.box(
        rx.box(
            rx.vstack(
                rx.heading(" Leasing de CPK ", size="8"),
                rx.heading("Inicio de sesión.", size="4"),
                align="center",
                spacing="4",
                padding="10px",
            ),
            
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    on_blur=AuthState.set_username,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                ),
                rx.button("Iniciar sesión", 
                          on_click=AuthState.login, 
                          size="3", 
                          width="100%"),
                spacing="4",
                align="center",
                padding="10px",
            ),
            rx.divider(),
            rx.vstack(
                rx.text(
                "¿Aún no tienes cuenta? ",           
                    ),
                rx.link("Regístrese para Empezar aquí.", 
                        href=Route.USERCONTACTO.value,
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
            spacing="4",
    )
    return base_page(
       mi_child,
       True
    )