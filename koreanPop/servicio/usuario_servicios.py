import bcrypt as bc
import reflex as rx
from ..respositorio.usuario_repositorio import select_all, select_userb_by_email

def select_all_user_service():
    users = select_all()
    print(users)
    return users

def auth_usuario(email: str, password: str):
    #buscar usuario
    user = select_userb_by_email(email)
    if(user == None):
        raise BaseException('El usuario no existe')
    if(not validate_password(password, user.password)):
        raise BaseException('Credenciales incorrectas')
    rx.LocalStorage("pruebatoken", name="TOKEN")
    rx.Cookie(name="pruebatoken", max_age=3600)
    return True

def validate_password(password: str, password_db:str):
    #hashed = bc.hashpw(password.encode('utf-8'), bc.gensalt())
    return bc.checkpw(password.encode('utf-8'), password_db.encode('utf-8'))