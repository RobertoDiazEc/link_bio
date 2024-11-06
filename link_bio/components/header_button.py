import reflex as rx
import link_bio.styles.styles as styles

def header_button(avatar: str, eslogan: str) -> rx.Component:
    return rx.container(
        
            rx.hstack(
                rx.avatar(fallback=avatar,
                    variant="solid",
                    ),
                rx.text(eslogan, style=styles.button_title_style)
            ),
            position="absolute", 
            top= "50%", 
            left= "50%", 
            transform= "translate(-50%, -50%)", 
            color= "white", 
            font_size= "24px", 
            font_weight= "bold", 
            background_color= "rgba(0, 0, 0, 0.5)", 
            padding="10px", 
            border_radius= "5px" ,    
 )