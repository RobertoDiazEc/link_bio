"""The authentication state."""
import reflex as rx
from sqlmodel import select
from ..models import UserSesion
from .base import baseState, ClienteL


class AuthState(baseState):
    """The authentication state for sign up and login page."""
    email:  str
    username: str
    password: str
    confirm_password: str

    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            if session.exec(select(ClienteL).where(ClienteL.email == self.email)).first():
                return rx.window_alert("Email ya existe.")
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords no es igual.")
            if session.exec(select(ClienteL).where(ClienteL.username == self.username)).first():
                return rx.window_alert("Username ya existe")
            self.user = ClienteL(clientel=self.username)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/")

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                select(ClienteL).where(ClienteL.username == self.username)
            ).first()
            if user and user.password == self.password:
                self.user = user
                return rx.redirect("/leasing")
            else:
                return rx.window_alert("Invalid username or password.")