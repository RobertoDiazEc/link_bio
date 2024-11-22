import reflex as rx
import link_bio.styles.styles as styles
from ..styles.styles import Size

def title( text: str) -> rx.Component:
    return rx.heading(
        text,
        size=Size.LARGE.value,
        style=styles.title_style

    )
