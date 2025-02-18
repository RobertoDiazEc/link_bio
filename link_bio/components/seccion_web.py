import reflex as rx
import link_bio.styles.styles as styles


def seccion_web(imgavatar: str, titulo: str, pie: str, url: str) -> rx.Component:
    return rx.box(
                rx.link(
                    rx.flex(
                        rx.icon(tag=imgavatar, size=35),
                        #rx.avatar(src=imgavatar),
                        rx.box(
                            rx.heading(titulo),
                            rx.text(pie ),
                           
                        ),
                        spacing="2",
                        flex_wrap="wrap",
                        align="center",
                        justify="center",
                    ),
                    #color_scheme="blue",
                    #background= "gray" ,
                    href=url,
                ),
        as_child=True,
        padding= "15px 1px",
        border=styles.Size.ZERO,
        # transform= "translate(-50%, -50%)", 
            #         color= "white", 
            #         font_size= styles.Size.DEFAULT, 
        font_weight= "bold", 
        #background_color= "rgba(150, 200, 200, 0.5)", 
            #         padding="15px 1px", 
        border_radius= "15px" ,
        width="80%"
    )
   