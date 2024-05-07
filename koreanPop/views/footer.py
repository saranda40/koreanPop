import reflex as rx
import koreanPop.styles.styles as styles
from koreanPop.styles.styles import Size, Color, TextColor
import datetime

def footer() -> rx.Component:
      return rx.hstack(
        rx.flex(
                rx.text("KoreanPop - Derechos Reservados © " + f"{yearencurso()}", align="center", as_="div"),
                direction="column",
                spacing="3",
                width="100%",
                color= TextColor.PRIMARY.value
            ),
        bg= Color.SECONDARY,
        color= Color.PRIMARY,
        padding="1em",
        height=Size.VERY_BIG.value,
        width="100%",
        z_index="5",
        bottom="0",
        position="fixed"
        )

def yearencurso() -> int:
        return datetime.date.today().year