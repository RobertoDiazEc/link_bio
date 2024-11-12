import reflex as rx
from link_bio.components.link_button import link_button
import link_bio.styles.styles as styles
import link_bio.constants  as Constants

def links() -> rx.Component:
    return rx.vstack(
        rx.heading("Servicios", style=styles.title_style),
        link_button("youtube", Constants.YOUTUBE_URL, "truck"),
        link_button("Programas", Constants.YOUTUBE_URL, "truck"),
        link_button("Propaganda", Constants.YOUTUBE_URL, "truck"),
        link_button("Proyectos", Constants.YOUTUBE_URL, "truck"),
    )

