import reflex as rx 

#from .stateLeasing import LeasingState
from ..ui.base_page import base_page


def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type
                ),
                as_child=True,
            ),
            direction="column",
           # spacing="1",
        ),
        name=name,
        width="100%",
    )


def signup_page() -> rx.Component:
   
   mi_child = rx.box(
       rx.card(
           rx.hstack(
                rx.badge(
                    rx.icon(tag="user-round-plus", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Registro de Usuarios",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Gracias por su Confianza",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                 height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
        rx.form.root(
           rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Datos Personales", value="tab1"),
                    rx.tabs.trigger("Datos Ingreso", value="tab2"),
                ),
                rx.tabs.content(
                  
                        rx.flex(
                            rx.flex(
                                form_field(
                                    "Nombres",
                                    "Nombres",
                                    "text",
                                    "nombres",
                                ),
                                form_field(
                                    "Apellidos",
                                    "Apellidos",
                                    "text",
                                    "apellidos",
                                ),
                                spacing="3",
                                flex_direction=[
                                    "column",
                                    "row",
                                    "row",
                                ],
                            ),
                            rx.flex(
                                form_field(
                                    "Email",
                                    "user@cpkm.com.co",
                                    "email",
                                    "email",
                                ),
                                form_field(
                                    "Celular", "Celular", "tel", "celular"
                                ),
                                spacing="3",
                                flex_direction=[
                                    "column",
                                    "row",
                                    "row",
                                ],
                            ),
                            direction="column",
                            spacing="2",
                            width="100%",
                        
                        ),
                    padding ="15px",
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.card(
                        form_field(
                            "Nombre Usuario",
                            "Username",
                            "text",
                            "username",
                        ),
                        form_field(
                            "Contraseña", "Password", "password", "clave"
                        ),
                        form_field(
                            "Confirmacion Contraseña", "Confirmar Password", "password", "conclave"
                        ),
                        size="3",
                        align="center",
                        padding ="36px",
                        width="50%",
                    ),   
                    rx.form.submit(
                            rx.button("Enviar",
                                    padding ="15px",
                                    width="50%",
                                    ),
                            as_child=True,
                        ),
                    value="tab2",
                ),
                padding ="15px",
                default_value="tab1",
           ),
                     
           
                   
            on_submit=lambda form_data: rx.window_alert(
                form_data.to_string()
            ),
            reset_on_submit=False,
        ),
         
        size="2",
        padding = "15px",
        border_radius="8px",
       ),
        size="3",
        align="center",
        padding ="36px",
        
           
        
    )
   return base_page(
       mi_child,
       hide_navbar=True,

    )