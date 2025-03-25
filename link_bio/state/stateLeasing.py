import reflex as rx      

from .base import baseState
from ..models import LeasingCli

class LeasingState(rx.State):
    Leasing_cli: LeasingCli = None
    username: str
    
    def Enviar_Submit(self, form_data:dict):
        print(form_data)