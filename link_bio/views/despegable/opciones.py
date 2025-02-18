import reflex as rx
import link_bio.styles.styles as styles

from .menurapido import semi_Menu

def opciones(titulo: str, detalle: str, imgopcion: str, masinfo: bool) -> rx.Component:
    return rx.card(
        rx.heading(titulo,
                   style=styles.title_style),
         rx.box(
                rx.text(detalle,
                        style=styles.title_body_style),
                rx.flex(        
                    rx.image(
                                    src=imgopcion, 
                                    width="50%", 
                                    height="auto",
                                    margin="10px",
                                ),
                    rx.cond(masinfo, 
                            semi_Menu(), 
                        #     rx.button("+ Informacion y Ejemplo Tarifario",
                        #             width="50%", 
                        #             height="auto",
                        #             on_click=baseState.check_login(),
                        #             ),
                            rx.divider()
                            ),       
                    spacing="2",
                    align="center",
                    justify="center",
                    direction="column",
                    flex_wrap="wrap",
                    width="100%",        
                ),                   
             padding= "10px 10px",             
            ),       
)