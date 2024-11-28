import reflex as rx
import link_bio.styles.styles as styles

def productos(proimg: str,titulo: str, detalle: str) -> rx.Component:
    return rx.card(
              rx.hstack(
                
                    rx.image(
                        src=proimg,
                        width="30%",
                        height="auto",
                        margin="10px",
                        ),
                   rx.vstack(
                    rx.heading(titulo,
                        style=styles.title_style),
                    rx.text(detalle,
                        style=styles.title_body_style),
                       
                    ),    
               align_items="center",
                ),
                
            width="5Ovw",
            padding= "10px 10px", 
            background_color= styles.Color.BACKGROUND.value,
              
        )