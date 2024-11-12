import reflex as rx

# Función que define el contenido dinámico basado en el estado
def app():
    # Estado para controlar qué contenido mostrar
    current_content = rx.state("home")

    # Función para actualizar el contenido cuando se selecciona una opción
    def update_content(content_name):
        current_content.set(content_name)

    # Contenido de cada sección
    content_map = {
        "home": "Bienvenido a la página de inicio.",
        "about": "Esta es la sección de información sobre nosotros.",
        "services": "Estos son nuestros servicios.",
        "contact": "Contáctanos por correo o teléfono.",
    }

    # Menú lateral
    sidebar = rx.column(
        rx.button("Inicio", on_click=lambda: update_content("home"), color_scheme="teal"),
        rx.button("Acerca de", on_click=lambda: update_content("about"), color_scheme="teal"),
        rx.button("Servicios", on_click=lambda: update_content("services"), color_scheme="teal"),
        rx.button("Contacto", on_click=lambda: update_content("contact"), color_scheme="teal"),
        spacing=2
    )

    # Contenido principal que se actualiza según el estado
    content_display = rx.text(content_map.get(current_content.get(), "Selecciona una opción"))

    # Estructura principal con el menú lateral y el contenido dinámico
    return rx.row(
        rx.box(sidebar, width="200px", height="100vh", bg="gray.100", p=4),
        rx.box(content_display, flex=1, p=4)
    )


