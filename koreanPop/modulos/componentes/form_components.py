import reflex as rx
from ...styles.styles import Size, Color

def campo_form_componente(label: str, placeholder: str, name_var: str,on_change_function, type_filed: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name_var,
                    type=type_filed,
                    required=True
                ),
                as_child=True,
            ),
            rx.form.message(
                "El campo no debe ser nulo",
                match="valueMissing",
                Color=Color.ALERTA.value,
            ),
            direction="column",
            spacing="2",
            align="stretch",
        ),
        name=name_var,
        width=Size.STANDARD.value
    )

def campo_form_componente_gral(label: str, placeholder: str, message_validate: str, name: str,on_change_function, show) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name,
                    required=True
                ),
                as_child=True
            ),
            rx.form.message(
                message_validate,
                name=name,
                match="valueMissing",
                force_match=show,
                color= Color.ALERTA.value,
            ),
            direction="column",
            spacing="2",
            align="stretch" 
        ),
        name=name,
        width=Size.STANDARD.value # Ancho del campo
    )