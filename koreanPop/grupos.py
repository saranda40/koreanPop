import reflex as rx
from koreanPop.styles.styles import Size, Color

@rx.page('/grupos',title='Grupos Musicales')
def grupos() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
            rx.heading("Grupos Musicales", size="9", color=Color.PRIMARY),
            rx.text("Agrupacion de Colores", align="center"),
            padding="30px"
            )
        )
    )