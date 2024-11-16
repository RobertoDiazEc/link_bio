import reflex as rx

# Estado para saber si las cookies han sido aceptadas
class CookieState(rx.State):
        cookies_aceptadas: bool = False
        c1: str = rx.Cookie()
        c2: str = rx.Cookie("c2 default")
        
        
        # Componente que muestra el banner de cookies
        def CookieBanner():
            return rx.box(
                #css={'position': 'fixed', 'bottom': '0', 'left': '0', 'right': '0', 'background-color': '#333', 'color': 'white', 'text-align': 'center', 'padding': '10px', 'font-size': '14px'},
               
                    rx.box(
                          rx.text('Usamos cookies para mejorar su experiencia. Al continuar navegando, acepta nuestra Política de Cookies.'),
                   rx.button('Aceptar', on_click=CookieState.accept_cookies),
                    rx.button('Rechazar', on_click=CookieState.reject_cookies)
           
                )
        )
        
        # Método para aceptar las cookies
        @rx.State.router
        def accept_cookies(state: CookieState):
            state.cookies_aceptadas = True

        # Método para rechazar las cookies
        @rx.State.router
        def reject_cookies(state: CookieState):
            state.cookies_aceptadas = False

# Componente principal de la aplicación
def main_cookie(state: CookieState):
    # Si las cookies no han sido aceptadas, mostrar el banner
    if not state.cookies_aceptadas:
        return rx.box(
                CookieState.CookieBanner(),  # Mostrar banner de cookies
               
        )
    