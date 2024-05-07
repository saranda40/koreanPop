import reflex as rx
from koreanPop.styles.styles import Size, Color


def menu()-> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.button(rx.icon(tag="users"),"Grupos"),
            rx.button(rx.icon(tag="user"), "Solistas"),
            rx.button(rx.icon(tag="user"), "Idols"),
            rx.button(rx.icon(tag="clapperboard"),"Actores"),
            rx.button(rx.icon(tag="clapperboard"),"Series"),
            rx.button(rx.icon(tag="clapperboard"),"Películas"),
        )
    )