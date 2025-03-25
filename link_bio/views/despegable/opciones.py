import reflex as rx
import link_bio.styles.styles as styles
from ..leasing.campos import action_button, button_link, action_link2
from ...ui.routes import Route

from .menurapido import semi_Menu

def opciones(titulo: str, detalle: str, imgopcion: str, masinfo: bool) -> rx.Component:
    return rx.card(
        rx.heading(titulo,
                   style=styles.title_style
                   ),    
       
                
                rx.flex(  
                    rx.flex( 
                        rx.text(detalle,
                            size= styles.SizeTxt.BIGN1.value,
                            style=styles.title_text_style
                            ),
                        action_link2(
                            "file-chart-column-increasing",
                            "Llenar Formulario",
                            Route.FORMULARIO.value,
                        ),
                        spacing="2",
                        width="100%",
                        direction="column",
                        align="center",  
                    ),         
                    rx.image(
                                    src=imgopcion, 
                                    width="50%", 
                                    height="auto",
                                    margin="10px",
                                ),
                         
                    spacing="2",
                    width="100%",
                    flex_direction=["column", "column", "row"],
                    align="center",        
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
             padding= "10px 10px", 
            background_color="#4b652a8a",            
                
)


def opciones2(titulo: str, detalle: str, detalle2: str, imgopcion: str) -> rx.Component:
    return rx.card(
        rx.heading(titulo,
                   style=styles.title_style
                   ),
                
            rx.flex( 
                rx.flex(
                    rx.text(detalle,
                        size= styles.SizeTxt.BIGN1.value,
                        style=styles.title_text_style
                    ),
                    rx.text(detalle2,
                        style=styles.title_text_style
                    ),
                    rx.hstack(
                    button_link(
                        "grip",
                        " Registrate",
                        rx.redirect(Route.USERCONTACTO),
                     ),
                    button_link(
                        "grip",
                        " Iniciar Sesión",
                        rx.redirect(Route.LEASING),
                     ), 
                    ),

                spacing="2",
                width="100%",
                direction="column",
                align="center",  
                ),             
                rx.image(
                    src=imgopcion, 
                    width="50%", 
                    height="auto",
                    margin="10px",
                ),
                spacing="2",
                width="100%",
                flex_direction=["column", "column", "row"],
                align="center",
                ),                   
             padding= "10px 10px", 
            background_color="#4b652a8a",            
     
)