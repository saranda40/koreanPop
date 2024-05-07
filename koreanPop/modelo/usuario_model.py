import reflex as rx
from typing import Optional
from sqlmodel import Field


class Usuario(rx.Model, table=True):
    ID: Optional[int]=Field(default=None, primary_key=True)
    Nombre: str
    Email: str
    Password: str
