import reflex as rx 

#from .stateLeasing import LeasingState
from ..ui.base_page import base_page
from ..state.auth  import AuthState
from ..state.navegar import CheckboxState
from ..ui.routes import Route

     

# class revisarFormulario(rx.State):

#     def update_feedback(self, email: str):
#         pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#         if re.match(pattern, email):
#             rx.window_alert("Correo válido")
#         else:
#             rx.window_alert("Correo no válido")

   
#     def submit_form(data):
#         email = data.get("email")
#         if revisarFormulario.update_feedback(email):
#             print("Correo válido:", email)
#         else:
#             print("Correo no válido")



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
            rx.flex(
                    rx.flex(
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Nombres", size="1"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="Nombres", 
                                        type="text",
                                        on_blur=AuthState.set_nombre,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="nombres",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Apellidos"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="Apellidos", 
                                        type="text",
                                        on_blur=AuthState.set_apellido,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="apellidos",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Email"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="user@cpkm.com.co", 
                                        type="email",
                                        on_blur=AuthState.set_email,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="email",
                            width="100%",
                        ),
                         rx.form.field(
                            rx.flex(
                                rx.form.label("Celular"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="099999999", 
                                        type="tel",
                                        on_blur=AuthState.set_celular,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="celular",
                            width="100%",
                        ),
                        spacing="1",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Nit-Rut"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="numero nit o rut", 
                                        type="text",
                                        max_length = 9,
                                        on_blur=AuthState.set_nitrut,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="email",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Nombre Empresa"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="Nombre Empresa", 
                                        type="text",
                                        on_blur=AuthState.set_nombre_empresa,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="celular",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Representante"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="Representante", 
                                        type="text",
                                        on_blur=AuthState.set_representante,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="celular",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Ciudad"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="ciudad", 
                                        type="text",
                                        on_blur=AuthState.set_ciudad,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="ciudad",
                            width="100%",
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
                rx.flex(
                    rx.card(
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Nombre Usuario"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="Username", 
                                        type="text",
                                        on_blur=AuthState.set_username,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="username",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Contraseña"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="Password", 
                                        type="password",
                                        min_length=8,
                                        max_length=25,
                                        on_blur=AuthState.set_password,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="clave",
                            width="100%",
                        ),
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Confirmar Contraseña"),
                                rx.form.control(
                                    rx.input(
                                        placeholder="Confirmar Password", 
                                        type="password",
                                        min_length=8,
                                        max_length=25,
                                        on_blur=AuthState.set_confirm_password,
                                    ),
                                    as_child=True,
                                ),
                                direction="column",
                            # spacing="1",
                            ),
                            name="conclave",
                            width="100%",
                        ),
                        size="3",
                        align="center",
                        padding ="36px",
                        width="100%",
                    ),
                    rx.card(                       
                         rx.vstack(
                            rx.link(
                                rx.text("Política de Privacidad y Uso de Datos", weight="bold", size="3"),
                                href=Route.PRIVACYPOLICY.value,
                                is_external=True,
                            ),
                            rx.text(
                                "Acepto el uso de mis datos para recibir informacion, publicidad, cotizaciones, facturas y que la información sea almacenada y recolectada en cualquier forma que proporcione conscientemente al llenar cualquier formulario en nuestro sitio web o con nosotros.",
                                size="2",
                                opacity=0.8,
                                align="center",
                            ),
                            rx.checkbox(
                            name="checkbox",
                            text="Acepto terminos y Condiciones",
                            on_change=CheckboxState.cambiocheck,
                            spacing="2",
                            ),
                         ),
                         
                        size="3",
                        align="center",
                        padding ="36px",
                        width="100%",
                    ),
                        name="politica",
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.form.submit(
                        rx.cond(
                            CheckboxState.boton,
                            rx.button("Enviar",
                                    padding ="15px",
                                    width="50%",
                                ),
                            ),
                            padding="15px",
                            as_child=True,
                        ),
                

            on_submit=AuthState.signup,
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