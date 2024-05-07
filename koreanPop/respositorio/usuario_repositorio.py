from ..modelo.usuario_model import Usuario
from .connet_db import connect
from sqlmodel import Session, select

def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Usuario)
        return session.exec(query).all()
    
def select_userb_by_email(email: str):
    engine = connect()
    with Session(engine) as session:
        query = select(Usuario).where(Usuario.Email == email)
        return session.exec(query).one_or_none()

