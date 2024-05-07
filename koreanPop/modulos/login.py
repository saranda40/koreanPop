import reflex as rx
import re
import asyncio

from .componentes.form_components import campo_form_componente, campo_form_componente_gral
from .componentes.notify_component import notify_component
from ..servicio.usuario_servicios import auth_usuario

@rx.page(route='/login', title='Login')
def login_page() -> rx.Component:
    return rx.section(
        rx.heading('Login')
         )

