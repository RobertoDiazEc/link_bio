import reflex as rx

from enum import Enum
from .colors import Color as Color
from .colors import TextoColor as TextColor

# Constantes
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO = "0em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.7em"
    BIG = "2em"

# Botton
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
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
             "background_color": "green",
            "color": "white",
        }
    }
}

title_style=dict(
    width="100%",
    padding_top=Size.LARGE.value,
    color=TextColor.HEADER.value
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