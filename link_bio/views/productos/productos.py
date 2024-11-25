import reflex as rx
import link_bio.styles.styles as styles

def productos(proimg: str,titulo: str, detalle: str) -> rx.Component:
    return rx.card(
              rx.flex(
                    rx.image(
                        src=proimg,
                        width="25%",
                        height="auto",
                        margin="10px",
                    ),
                    rx.hstack(
                    rx.heading(titulo,
                        style=styles.title_style),
                    rx.text(detalle,
                        style=styles.title_body_style),
                    ),    
                ),
                
            width="5Ovw",
            padding= "10px 10px", 
        )