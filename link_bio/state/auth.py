"""The authentication state."""
import reflex as rx
from datetime import datetime
import re
import bcrypt

import asyncio
from ..ui.routes import Route
from sqlmodel import select
from ..models import UserSesion
from .base import baseState, ClienteL


class AuthState(baseState):
    """The authentication state for sign up and login page."""
    User_Sesion: UserSesion = None
    useregistro: str = rx.LocalStorage("",sync= True)
    nombre: str
    apellido: str
    email:  str
    celular: str
    ciudad: str
    username: str
    password: str
    confirm_password: str
    nombre_empresa: str
    nitrut: str
    representante: str

    @rx.event
    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(pattern, self.email):
                return rx.window_alert("Correo no válido")
            if session.exec(select(ClienteL).where(ClienteL.email == self.email)).first():
                return rx.window_alert("Email ya existe.")
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords no es igual.")
            if session.exec(select(ClienteL).where(ClienteL.username == self.username)).first():
                return rx.window_alert("Username ya existe")
            if not re.match(r'[0-9]+$', self.nitrut):
                return rx.window_alert("Nit solo se permite numeros")

            code_password =  bcrypt.hashpw(self.password.encode(), bcrypt.gensalt())
            self.password = code_password.decode() 
            self.user = ClienteL(
                nombre=self.nombre,
                apellido=self.apellido,
                email=self.email,
                celular=self.celular,
                ciudad=self.ciudad,
                username=self.username,
                password=self.password,
                nombre_empresa=self.nombre_empresa,
                nitrut=self.nitrut,
                representante=self.representante,              
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                )
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            self.useregistro = "T"
            return rx.redirect(Route.LEASING.value)
    
    @rx.event
    def reset_login(self):
         with rx.session() as session:
            
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(pattern, self.email):
                return rx.window_alert("Correo no válido")
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords no es igual.")
            
            user = session.exec(select(ClienteL).where(ClienteL.email == self.email)).first()
            if user:
                code_password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt())
                user.password = code_password.decode()
                session.add(user)
                session.commit()
                user = None    
                rx.window_alert("Contraseña Cambiada con Exito!")
                return (rx.redirect(Route.INDEX.value))