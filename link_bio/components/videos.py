import reflex as rx


def videos(urlv: str) -> rx.Component:
    return rx.box(
        rx.video(
            url=urlv,
            width="400px",
            height="auto",
            type="/mp4"
        ),
    )    