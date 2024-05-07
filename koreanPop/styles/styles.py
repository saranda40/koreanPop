import reflex as rx
from enum import Enum
from .font import Font
from .color import Color, TextColor

MAX_WIDTH = "1000px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY,
    "background": Color.PRIMARY
}

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "4em"
    STANDARD = "30vw"
    XS="xs"

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)