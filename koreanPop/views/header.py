import reflex as rx
import koreanPop.styles.styles as styles
from koreanPop.styles.styles import Size, TextColor
from koreanPop.views.menu import menu

def header() -> rx.Component:
    return rx.vstack(
            rx.heading("KoreanPop, tu espacio sobre el espectáculo de Corea"
                       , size="9"
                       , padding_botton= Size.DEFAULT.value
                       , align="center"),
            rx.flex(
                rx.text("Tu votación es importante para nosotros! ", align="center", as_="div"),
                direction="column",
                spacing="3",
                width="100%",
                color= TextColor.PRIMARY.value
            ),
             padding_top=Size.VERY_BIG.value,
             style=styles.max_width_style,
             margin_left="200px",
    )
    
