import reflex as rx

from ..state.auth import AuthState
from ..state.navegar import CheckboxState
from ..ui.base_page import base_page
from ..ui.routes import Route

def resetear_page() -> rx.Component:
    """The login page."""
    mi_child= rx.box(
        rx.box(
            rx.vstack(
                rx.heading(" RESET CONTRASEÑA ", size="8"),
                rx.heading("confirmar tu correo ", size="4"),
                align="center",
                spacing="4",
                padding="10px",
            ),
            
            rx.vstack(
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    type="email",
                    placeholder="email",
                    on_blur=AuthState.set_email,
                    size="3",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    type="password",
                    placeholder="Confirmar Password",
                    on_blur=AuthState.set_confirm_password,
                    size="3",
                    width="100%",
                ),
                rx.button("Actualizar Clave", 
                        on_click=AuthState.reset_login,
                        size="3", 
                        width="100%"
                    ),
                rx.divider(),
                
                
                
                spacing="4",
                #align="center",
                padding="45px",
            ),
            rx.divider(),
            rx.vstack(
                rx.text(
                "El proceso termina cuando se redireccione a la pagina principal ",           
                    ),
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