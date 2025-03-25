import reflex as rx

import link_bio.styles.styles as style

def header_base(srcimagen: str) -> rx.Component:
    return rx.box( 
          rx.image(
                src=srcimagen, 
                width="100%", 
                height="50%",
                auto="format",
                ),
            position= "relative",
            width="100%"
    )       


def header_base_img(srcimagen: str) -> rx.Component:
    return rx.image(
            src=srcimagen, 
            width="100%",
            height="auto",
            auto="format", 
            opacity=0.5,
        )
    # ,
    #     border_radius="15px",
    #     box_shadow="0 25px 50px rgba(0, 0, 0, 0.3)",
    #     background_size="cover",    #/"cover","contain"
    #     background_position="center",
    #     #background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)"
    #     width="100%"
    # )    