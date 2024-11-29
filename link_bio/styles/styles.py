import reflex as rx

from enum import Enum
from .colors import Color as Color
from .colors import TextoColor as TextColor
from .fonts import Font, FontWeight


# Constantes
MAX_WIDTH = "560px"
MED_WIDTH = "300px"
MIN_WIDTH = "100px"


#fond sheets

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght500&display=swap"
]

# Sizes
class Size(Enum):
    ZERO = "0em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    BIGN1 ="3em"

# Botton
# "font_family": Font.DEFAULT.value,
# "font_weight": Font
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,    
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration" : "none",
        "_hover" : {
             #"background_color": Color.SECONDARY.value,
             "background_color": Color.CONTENT.value,
            "color": Color.PRIMARY.value,
        }
    }
}

title_style=dict(
    width="100%",
    padding_top=Size.MEDIUM.value,
    padding=Size.MEDIUM.value,
    color=TextColor.HEADER.value,
    
)

title_header_style=dict(
    width="100%",
    color=Color.BACKGROUND.value
)

title_body_style=dict(
    width="100%",
    padding="1em",
    color=TextColor.BODY.value
)

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Size.SMALL.value
)

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)



# Definir la clase CSS para el navbar
navbar_css = """
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    transition: background-color 0.3s ease;
}
.navbar.transparent {
    background-color: rgba(255, 255, 255, 0);
}
.navbar.dark {
    background-color: rgba(0, 0, 0, 0.8);
}
"""

# Añadir el JavaScript
navbar_js = """
window.onscroll = function() {
    var navbar = document.querySelector('.navbar');
    if (window.pageYOffset > 50) {
        navbar.classList.remove('transparent');
        navbar.classList.add('dark');
    } else {
        navbar.classList.remove('dark');
        navbar.classList.add('transparent');
    }
};
"""

base_navbar = dict( 
    position= 'fixed', 
    top= '0',
    widt= '100%',
    transition= 'background-color 0.3s ease',
)

base_navbar_transparent = dict( 
    background_color= 'rgba(255, 255, 255, 0)',
) 

base_navbar_dark= dict ( 
    background_color= 'rgba(0, 0, 0, 0.8)',
)