import reflex as rx

class AlertDialogState2(rx.State):
    opened: int = 0

    @rx.event
    def dialog_open(self):
        self.opened = 1

def alert_dialog2(opened=False) -> rx.Component:
    
    if opened == 1:
        return rx.box(rx.text("ok"))
    else: 
        return rx.box(
            rx.text("politica de calidad"),
            rx.text(""" Utilizamos cookies para mejorar tu experiencia en nuestro sitio web. Al continuar navegando en este sitio, aceptas el uso de cookies. Puedes obtener más información en nuestra [Política de Privacidad](#). """), 
            rx.button(
            "Aceptar",
            on_click=AlertDialogState2.dialog_open,
        

        ),
        style={"position": "fixed",
                   "bottom": "20px", 
                   "right": "20px", 
                   "z-index": "1000"}
    )