"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from link_bio.styles import styles
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index():
    return rx.fragment(
        rx.vstack(
            rx.heading("This is a header"),
            rx.center("This text is centered"),
            rx.button(
                "click me",
                on_click=rx.toast("show toast!"),
                bg="purple",
                border_radius="0.5em",
                pl="10px",
            ),
        ),
    )


app = rx.App()
app.add_page(index)
app._compile()