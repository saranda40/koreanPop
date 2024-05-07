import reflex as rx
from koreanPop.styles.styles import Size, Color

@rx.page('/admin',title='Administrador Sitio')
def admin() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
   
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )