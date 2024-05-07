from rxconfig import config
from koreanPop.views.navbar import navbar
from koreanPop.views.menu import menu
from koreanPop.views.header import header
from koreanPop.views.sidebar import sidebar
from koreanPop.views.footer import footer
from koreanPop.styles.styles import Size
import koreanPop.styles.styles as styles

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(  
                sidebar(),
                header(),  
                rx.logo(),
                align="center",
                spacing="7",
                font_size=Size.BIG,
            )
        ),
        footer(),
    )

app = rx.App()
app.add_page(index)
