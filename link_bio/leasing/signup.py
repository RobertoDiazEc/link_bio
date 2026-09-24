import reflex as rx

from ..state.auth import AuthState
from ..state.navegar import CheckboxState
from ..ui.base_page import base_page
from ..ui.routes import Route


def signup_page() -> rx.Component:
    """Render the user registration form."""
    identity_fields = rx.flex(
        rx.input(placeholder="Nombres", type="text", name="nombre", required=True),
        rx.input(placeholder="Apellidos", type="text", name="apellido", required=True),
        rx.input(placeholder="user@cpkm.com.co", type="email", name="email", required=True),
        rx.input(placeholder="099999999", type="tel", name="celular", required=True),
        spacing="3",
        direction="column",
        width="100%",
    )

    company_fields = rx.flex(
        rx.input(
            placeholder="numero nit o rut",
            type="text",
            name="nitrut",
            max_length=9,
            required=True,
        ),
        rx.input(placeholder="Nombre Empresa", type="text", name="nombre_empresa"),
        rx.input(placeholder="Representante", type="text", name="representante"),
        rx.input(placeholder="ciudad", type="text", name="ciudad", required=True),
        spacing="3",
        direction="column",
        width="100%",
    )

    account_fields = rx.card(
        rx.input(placeholder="Username", type="text", name="username", required=True),
        rx.input(
            placeholder="Password",
            type="password",
            name="password",
            min_length=8,
            max_length=25,
            required=True,
        ),
        rx.input(
            placeholder="Confirm Password",
            type="password",
            name="confirm_password",
            min_length=8,
            max_length=25,
            required=True,
        ),
        size="3",
        align="center",
        padding="36px",
        width="100%",
    )

    terms = rx.card(
        rx.vstack(
            rx.link(
                rx.text("Política de Privacidad y Uso de Datos", weight="bold", size="3"),
                href=Route.PRIVACYPOLICY.value,
                is_external=True,
            ),
            rx.text(
                "Acepto el uso de mis datos para recibir informacion, publicidad, "
                "cotizaciones, facturas y que la información sea almacenada y "
                "recolectada en cualquier forma que proporcione conscientemente al "
                "llenar cualquier formulario en nuestro sitio web o con nosotros.",
                size="2",
                opacity=0.8,
                align="center",
            ),
            rx.checkbox(
                name="terms",
                text="Acepto terminos y Condiciones",
                on_change=CheckboxState.cambiocheck,
                required=True,
                spacing="2",
            ),
            spacing="3",
            align="center",
        ),
        size="3",
        align="center",
        padding="36px",
        width="100%",
    )

    form = rx.form(
        rx.flex(
            rx.card(
                rx.grid(
                    identity_fields,
                    company_fields,
                    columns=rx.breakpoints(initial="1", md="2"),
                    spacing="5",
                    width="100%",
                ),
                width="100%",
            ),
            rx.grid(
                account_fields,
                terms,
                columns=rx.breakpoints(initial="1", md="2"),
                spacing="5",
                width="100%",
            ),
            direction="column",
            spacing="5",
            width="100%",
        ),
        rx.button(
            "Enviar",
            type="submit",
            disabled=~CheckboxState.boton,
            padding="15px",
            width=rx.breakpoints(initial="100%", md="50%"),
        ),
        on_submit=AuthState.signup,
        reset_on_submit=False,
    )

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
                    rx.heading("Registro de Usuarios", size="4", weight="bold"),
                    rx.text("Gracias por su Confianza", size="2"),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align="center",
                width="100%",
            ),
            form,
            size="2",
            padding="15px",
            border_radius="8px",
        ),
        size="3",
        align="center",
        padding=rx.breakpoints(initial="1", sm="4", md="9"),
    )

    return base_page(mi_child, hide_navbar=True)
