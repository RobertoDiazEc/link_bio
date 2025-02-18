import reflex as rx      

class LeasingState(rx.state):

    def Enviar_Submit(self, form_data:dict):
        print(form_data)