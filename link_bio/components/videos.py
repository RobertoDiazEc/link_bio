import reflex as rx


def videos(urlv: str) -> rx.Component:
    return rx.box(
        rx.video(
            src=urlv,
            width="400px",
            height="auto",
            playing=True,
        ),
    )    