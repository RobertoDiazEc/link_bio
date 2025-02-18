import reflex as rx

@rx.page(route='/informar', title="My Beautiful App")

def informar() -> rx.Component:
    # Welcome Page (Index)
    return rx.fragment(
        rx.center(
            rx.vstack(
                rx.heading('Informar', size='8'),
                rx.text("Mi pagina informar")
            )            
        )
    )