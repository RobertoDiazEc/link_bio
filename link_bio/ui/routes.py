from enum import Enum

class Route(Enum):
    INDEX = "/"
    CONTACTOS = "/contactos"
    PRODUCTOS = "/productos"
    COMUNIDAD = "/comunidad"
    REGISTRATE = "/protected"
    SERVICIOS = "/servicios"
    PRIVACYPOLICY = "/protected/privacy_policy"
    APPLEASING = "/app"
    LEASING = "/leasing"
    LOGINCPK = "/login"
    USERCONTACTO = "/signup"
    RESETKEY = "/resetear"
    PDFVIEWER = "/pdf/mostrar_pdf"
    PDFVIEW2 = "/mostrar_pdf"
    API_PDF= "http://localhost:8000/api/contrato-pdf/"
    FORMULARIO = ""
    


