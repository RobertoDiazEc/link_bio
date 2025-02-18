"""Base state for Twitter example. Schema is inspired by https://drawsql.app/templates/twitter."""
from typing import Optional

import reflex as rx
from ..ui.routes import Route
from ..models import ClienteL

class baseState(rx.State):
    """The base state for the app."""

    user: Optional[ClienteL] = None

    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect(Route.LEASING)

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect(Route.LOGINCPK)

    @rx.var
    def logged_in(self) -> bool:
        """Check if a user is logged in."""
        return self.user is not None