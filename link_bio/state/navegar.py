import reflex as rx



class CheckboxState(rx.State):
    checked: bool = False
    boton: bool = False

    @rx.event
    def on_load(self, estado: bool):
        self.checked = False
        self.boton = False
        
    @rx.event  
    def cambiocheck(self, valorchek: bool):
        self.checked = valorchek
        if valorchek:
            self.boton = True
        else:
            self.boton = False

    


class redirpage(rx.State):

    def page_destino(self, rute: str):
        return rx.redirect(rute)
    
    def mensaje_page(self, texto: str):
        return rx.window_alert(texto)