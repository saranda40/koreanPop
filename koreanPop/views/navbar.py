import reflex as rx
from koreanPop.styles.styles import Size, Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("KoreanPop - Votación de Artistas y Músicos de Corea"),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Menu"),
            ),
            rx.menu.content(
                rx.menu.item("Inicio"),
                rx.menu.separator(),
                rx.menu.item("Ingresar"),
                rx.menu.item("Contacto"),
            ),
            width="100%"
        ),
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
        )


        