import reflex as rx
from koreanPop.styles.styles import Size, Color
from koreanPop.views.menu import menu

def sidebar() -> rx.Component:
    return rx.vstack(
        rx.heading("KoreanPop", margin_bottom="10px"),
        rx.list.ordered(
            rx.list.item(rx.link("Grupos Musicales",href="/grupos.py")),
            rx.list.item("Cantantes"),
            rx.list.item("Actores"),
            rx.list.item("Deportistas"),
            rx.list.item("Actrices"),
            rx.list.item("Directores"),
            list_style_type="none",
            
        ),
        position="fixed",
        height="90%",
        left="0px",
        top="62px",
        z_index="5",
        padding_x="10px",
        padding_y="1em",
        background_color=Color.TERTIARY.value,
        align_items="left",
        width="200px",
    )