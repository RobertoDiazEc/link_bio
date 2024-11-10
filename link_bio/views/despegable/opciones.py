import reflex as rx

def opciones() -> rx.Component:
    return rx.box(
        rx.heading("Recoleccion de Datos"),
         rx.box(
                rx.text("Nuestro personal tecnico visitara las instalaciones donde el cliente los necesite, para realizar la respectiva verificacion de los datos"),
                rx.image(
                                src="/imagen/servicio2.jpg", 
                                width="70%", 
                                height="auto",
                                auto="format",
                            ),
            ),
     width="100%",   
)