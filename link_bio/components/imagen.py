import reflex as rx
import link_bio.styles.styles as styles

def imagen(imagenes: str, titulo: str, detalle: str) -> rx.Component:
    return rx.box( 
        rx.image(
                src=imagenes, 
                width="100%", 
                height="auto",
                auto="format",
        ),
        rx.container(
            rx.hstack(
                rx.box(
                    rx.text(titulo, style=styles.button_title_style),
                ),
                rx.box(
                rx.text(detalle, style=styles.button_title_style),
                ),
            ),
            position="absolute", 
            top= "50%", 
            left= "50%", 
            transform= "translate(-50%, -50%)", 
            color= "white", 
            font_size= "14px", 
            font_weight= "bold", 
            background_color= "rgba(0, 0, 0, 0.5)", 
            padding="10px", 
            border_radius= "5px" ,    
         ),
    position= "relative",
    width="100%",
    )       