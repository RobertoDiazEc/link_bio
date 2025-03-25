import reflex as rx
from datetime import datetime, timedelta
from typing import Union, List
import os

from pathlib import Path
import bcrypt
from decouple import config
import re 
from jinja2 import Environment

import os.path as path
from .PdfJS import PDFJavascript as FPDF
from sqlmodel import String, asc, cast, desc, func, or_, select
from ..views.empresa.empresadet import EmpresaContratoCpk
from ..ui.routes import Route
from ..models import ClienteL, UserSesion, LeasingCli, Dimensiones, Tipo_Vehiculo, Servicio, Operacion, Sector, Tarifas

ROUTEAPI_PDF = config("ROUTEAPI_PDF")
ROUTEANEXO2 = config("ROUTEANEXO2")

class backState(rx.State):
    """The base state for the app."""
    meses_anio: dict = {
    "January": "Enero",
    "February": "Febrero",
    "March": "Marzo",
    "April": "Abril",
    "May": "Mayo",
    "June": "Junio",
    "July": "Julio",
    "August": "Agosto",
    "September": "Septiembre",
    "October": "Octubre",
    "November": "Noviembre",
    "December": "Diciembre"
    }
    users: list[ClienteL] = []
    user_actual: ClienteL = ClienteL()
    cliente_sesion: UserSesion = UserSesion()
    leasing_cliente: LeasingCli = LeasingCli()
    tarifas_cliente: Tarifas = Tarifas()
    outfilepdf: str = ""
    name_imagen: str = ""
    mes_actual: str =""

    acceso_key: bool = False
    acceso_auth: bool = False
    check_empresa_acepta: bool = False
    num_intentos: int = 0
    calculo_tarifa: float = 0
    dimensionesall: List[str] = []
    tipoVehiculoall: List[str] = []
    servicioall: List[str] = []
    operacionall: List[str] = []
    sectorall: List[str] = []

    val_tipo_vehiculo: str =""
    val_operacion: str =""
    val_servicio: str =""
    val_sector: str =""
    val_dimension: str =""
    val_kilometros: str ="0"

    @rx.event
    def on_load(self):
        self.user_actual = ClienteL()
        self.cliente_sesion = UserSesion()
        self.leasing_cliente = LeasingCli()
        self.tarifas_cliente = Tarifas()
        self.acceso_key = False
        self.check_empresa_acepta = False
        self.num_intentos = 0
        self.calculo_tarifa = 0
        self.outfilepdf=""
        self.mes_actual=self.nombre_mes(datetime.now().strftime("%B"))
        with rx.session() as session:
            self.dimensionesall= session.exec(select(Dimensiones.nombre).where()).all()
            self.tipoVehiculoall= session.exec(select(Tipo_Vehiculo.nombre).where()).all()
            self.servicioall= session.exec(select(Servicio.name).where()).all()
            self.operacionall= session.exec(select(Operacion.nombre).where()).all()
            self.sectorall= session.exec(select(Sector.nombre).where()).all()
            
                        
    def logout(self):
        """Log out a user."""
        self.reset()
        self.clear_exit()
        return rx.redirect(Route.INDEX)

    def check_login(self):
        """Check if a user is logged in."""
        #print(self.user_actual.id)
        if self.user_actual.id == None:
            return rx.redirect(Route.LOGINCPK)
        
    def clear_exit(self):
        self.users = []
        self.user_actual = ClienteL()
        self.cliente_sesion = UserSesion()
        self.tarifas_cliente= Tarifas()
        self.dimensionesall= []
        self.acceso_key = False
        self.num_intentos = 0
        self.acceso_auth= False 

    def nombre_mes(self, mes_ingles: str):
        return self.meses_anio.get(mes_ingles, "Mes no válido")
    
    @rx.event
    def intentos_permitidos(self):
        self.num_intentos = self.num_intentos + 1
            
    @rx.event
    async def imagen_placa(self, files: list[rx.UploadFile]):
        """Manejar la subida de archivo(s).
        Args:
            files: Los archivos subidos.
        """
        current_file = files[0]
        upload_data = await current_file.read()
        outfile = (
            rx.get_upload_dir() / current_file.name
        )

        # Guardar el archivo
        with outfile.open("wb") as file_object:
            file_object.write(upload_data)

        # Actualizar la variable del archivo
        self.name_imagen = current_file.name    
        #print("subir imagen")

    @rx.event
    async def imagen_placa_borrar(self, files: list[rx.UploadFile]):
        """Manejar la subida de archivo(s).
        Args:
            files: Los archivos subidos.
        """
        current_file = files[0]
        outfile = (
            rx.get_upload_dir() / current_file.name
        )

        # Guardar el archivo
        if os.path.exists(outfile):
            os.remove(outfile)

        # Actualizar la variable del archivo
        self.name_imagen = ""
        rx.clear_selected_files("upload1")    
        #print("borrada imagen")       
   
    @rx.event
    def sumit_login(self, form_data: dict):
        #self.clear_exit()
        self.login(form_data)
        #yield
        if self.acceso_key and self.acceso_auth:
            return rx.redirect(Route.LEASING.value)
        else:    
            self.intentos_permitidos()
            
            if self.num_intentos > 3:
                #print(self.num_intentos)
                rx.window_alert("Limite de Intentos NO VALIDOS, superado.  ... ")
                self.clear_exit()
                return rx.redirect(Route.INDEX.value)
            return rx.window_alert(f"Invalido username o password. Vuelva a intentarlo por {self.num_intentos}")
        
    @rx.event
    def login(self, form_data: dict):
        """Log in a user."""        
        entr_username = form_data.get("username")
        entr_password = form_data.get("password")
        #print(form_data)
        try:
            with rx.session() as session:
                obj = session.exec(select(ClienteL).where(ClienteL.username == entr_username)).first()

            if obj:
                code_password = obj.password
                if bcrypt.checkpw(entr_password.encode(), code_password.encode()):
                    self.acceso_key = True
                    self.user_actual=obj  
                    self.crear_session()                          
                    
                else:
                    self.acceso_key = False
                    
        except Exception as e:       
            return rx.window_alert(f"Ingreso Login-Usuario {form_data.get("username")}, error:--> {e}")

    @rx.event
    def crear_session(self):
        self.acceso_auth= True
        if self.cliente_sesion.id == None and self.acceso_key:
            with rx.session() as session: 
                obj = UserSesion(
                    nombrelogin=self.user_actual.username, 
                    cliente_id=self.user_actual.id,
                    created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
                session.add(obj)
                session.commit()
                session.refresh(obj)
                self.cliente_sesion= obj
                #print(obj, obj.id)
                rx.toast.info(
                    f"User {self.cliente_sesion.nombrelogin} iniciando session.", position="bottom-right"
                    )

    @rx.event
    def actualizacliente(self, form_data: dict):
        with rx.session() as session:
            cliente = session.exec(
                ClienteL.select().where(
                    (ClienteL.id == self.user_actual.id)
                )
            ).first()
            cliente.nombre_empresa = form_data.get("nombre_empresa")
            cliente.nitrut = form_data.get("nitrut")
            cliente.representante = form_data.get("representante")
            session.add(cliente)
            session.commit() 
        
        return rx.toast("Registro Actualizado.")
                
    @rx.event(background=True)
    async def grabar_leasing(self, form_data: dict):
        """Crear Leasing ingresado los datos y dimensiones."""
        async with self:
            pattern = r'[a-zA-Z]{1}'
            if not re.match(pattern, form_data.get("placa")):
                return rx.window_alert("Numero de Placa No Valida")
            if int(self.val_kilometros) < 4000:
                return rx.window_alert("Kilometros no puede ser menor a 4000 Km/mes")
            if self.calculo_tarifa == 0:
                return rx.window_alert("Calcular Tarifa antes de grabar.")
            
            with rx.session() as session:          
                obj= LeasingCli(
                        usersesion_id=self.cliente_sesion.id,
                        tarifa_id=self.tarifas_cliente.id,
                        username= self.user_actual.username,
                        leasing=self.tarifas_cliente.valor,
                        ruta= "normal",
                        Precio_cal= 0,
                        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        **form_data
                    )
                session.add(obj)
                session.commit()
                session.refresh(obj)
                self.leasing_cliente=obj
                rx.window_alert("Registro creado exitosamente.")

    @rx.event
    def change_value_tipo(self, value: str):
        """Change the select value var."""
        self.val_tipo_vehiculo = value
        self.clear_selected()
        self.llenar_operaciones() 

    @rx.event
    def change_value_operacion(self, value: str):
        """Change the select value var."""
        self.val_operacion = value
        self.llenar_dimensiones()
    
    @rx.event
    def change_value_servicio(self, value: str):
        """Change the select value var."""
        self.val_servicio = value 

    @rx.event
    def change_value_sector(self, value: str):
        """Change the select value var."""
        self.val_sector = value 

    @rx.event
    def change_value_dimension(self, value: str):
        """Change the select value var."""
        self.val_dimension = value 

    @rx.event
    def llenar_dimensiones(self):

        with rx.session() as session:
            #self.skills= session.exec(select(Dimensiones.nombre).where()).all()
            self.dimensionesall= session.exec(select(Tarifas.dimension).where(
                (Tarifas.tipo == self.val_tipo_vehiculo)).where( Tarifas.operacion == self.val_operacion)
                ).all()
       # print(self.dimensionesall)

    @rx.event
    def llenar_operaciones(self):
    
        with rx.session() as session:
        #self.skills= session.exec(select(Dimensiones.nombre).where()).all()
            self.operacionall= session.exec(select(Tarifas.operacion).distinct().where(
                (Tarifas.tipo == self.val_tipo_vehiculo))
                ).all()
        #print(self.operacionall)       

    @rx.event
    def clear_selected(self):
        self.dimensionesall.clear()
        self.operacionall.clear()

    @rx.event
    def limpiar_pantalla(self):
        self.dimensionesall.clear()
        self.operacionall.clear()
        self.calculo_tarifa=0
        self.leasing_cliente=LeasingCli()  

    @rx.event
    def calcular_tarifa(self):
        if int(self.val_kilometros) < 4000:
            return rx.window_alert("Lamentamos no tener establecida una tarifa para su operación en el momento")
        if self.val_sector == "Minería":
            return rx.window_alert("Lamentamos no tener establecida una tarifa para su operación en el momento")
        if self.val_sector == "Agrícola":
            return rx.window_alert("Lamentamos no tener establecida una tarifa para su operación en el momento")
        
        with rx.session() as session:
            #self.skills= session.exec(select(Dimensiones.nombre).where()).all()
            sentencia=select(Tarifas).where(
                (Tarifas.tipo == self.val_tipo_vehiculo), 
                (Tarifas.operacion == self.val_operacion),
                (Tarifas.dimension == self.val_dimension))
            obj = session.exec(sentencia).first()
            self.tarifas_cliente= obj
            self.calculo_tarifa= self.tarifas_cliente.valor
            
        #print(self.calculo_tarifa)  

    @rx.event
    def generar_pdfjs(self):
        nombrearchivo=f"{self.leasing_cliente.id}-{self.cliente_sesion.id}-{self.user_actual.username}_contrato.pdf"
        fechacontrato=f"Bogotá, {datetime.now().strftime("%d")} de {self.mes_actual} del {datetime.now().strftime("%Y")}"
        env= Environment()
        texto1= env.from_string(EmpresaContratoCpk.CONTRATODETALLETITULO.value)
        textonuevo=texto1.render(
            nombrempresa = self.user_actual.nombre_empresa,
            nitempres = self.user_actual.nitrut,
            nombrerepresentante = self.user_actual.representante,
            tarifavalor = self.calculo_tarifa
        )
        num_contrato= env.from_string(EmpresaContratoCpk.CONTRATONUMERO.value)
        contratonumgenerado=f"CPK{self.leasing_cliente.id}-{self.cliente_sesion.id}"
        num_contrato_nuevo=num_contrato.render(
            numerocontrato = contratonumgenerado,
        )
        textoA= env.from_string(EmpresaContratoCpk.CONTRATOCLAUSULASA.value)
        textonuevoA=textoA.render(
            nombrempresa = self.user_actual.nombre_empresa,
            tarifavalor = self.calculo_tarifa
        )
        textoB= env.from_string(EmpresaContratoCpk.CONTRATOCLAUSULASB.value)
        textonuevoB=textoB.render(
            nombrempresa = self.user_actual.nombre_empresa,           
        )
        nombre_representante=self.user_actual.representante
        nombreimagen=f"{ROUTEANEXO2}Anexo2cpk.png"
        outfile = Path(rx.get_upload_dir()) / nombrearchivo
        pdf = FPDF()
        pdf.set_title("CPK - Arrendamiento")
        pdf.set_author("CPK-REDx Soluciones")
        pdf.add_page()
        pdf.set_left_margin(25)
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0,10, txt=EmpresaContratoCpk.CONTRATOTITULO.value, ln=True, align="C")
        pdf.ln(5)
        pdf.cell(0, 6, txt=fechacontrato, ln=True, align="L")
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(170, 6, txt=textonuevo)
        pdf.ln(2)
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 6, txt=num_contrato_nuevo, ln=True, align="L")
        pdf.ln(1)
        pdf.multi_cell(50, 6, txt=EmpresaContratoCpk.CONTRATOCLAUSULAS.value)
        pdf.ln()
        pdf.set_font("Arial", size=12)        
        pdf.multi_cell(170, 6, txt=textonuevoA)
        pdf.ln()
        pdf.multi_cell(170, 6, txt=textonuevoB)
        pdf.ln()
        pdf.multi_cell(170, 6, txt=EmpresaContratoCpk.CONTRATOCLAUSULASC.value)
        pdf.ln(3)
        pdf.cell(0, 6, txt="Firman:", ln=True, align="L")
        pdf.ln(12)
        pdf.cell(10, 6, txt="________________________",align="L")
        pdf.set_x(120)
        pdf.cell(140, 6, txt="________________________",align="L")
        pdf.ln()
        pdf.set_font("Arial","B", size=10)
        pdf.cell(10, 6, txt="CARLOS ALBERTO LEALGONZALEZ",align="L")
        pdf.set_x(120)
        pdf.cell(140, 6, txt=nombre_representante.upper(),align="L")
        pdf.ln()
        pdf.cell(10, 6, txt="NIT 79984801-2",align="L")
        pdf.set_x(120)
        pdf.cell(140, 6, txt=self.user_actual.nombre_empresa,align="L")
        pdf.add_page()
        pdf.set_left_margin(25)
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0,10, txt="ANEXO 1  LISTADO DE VEHICULOS", ln=True, align="C")
        pdf.ln(6)
        pdf.set_xy(22.0, 30.0)
        pdf.set_line_width(0.0)
        pdf.line(15.0, 28.0, 195.0, 28.0)
        pdf.line(15.0, 28.0, 15.0, 102.0)
        pdf.set_xy(25.0, 30.0)
        pdf.cell(ln=0, h=5.0, align='L', w=5.0, txt='Placa', border=0)
        pdf.line(50.0, 28.0, 50.0, 102.0)
        pdf.set_xy(55.0, 30.0)
        pdf.cell(ln=0, h=5.0, align='L', w=25.0, txt='Tipo Vehiculo', border=0)
        pdf.line(90.0, 28.0, 90.0, 102.0)
        pdf.set_xy(95.0, 30.0)
        pdf.cell(ln=0, h=5.0, align='L', w=25.0, txt='Operación', border=0)
        pdf.line(120.0, 28.0, 120.0, 102.0)
        pdf.set_xy(125.0, 30.0)
        pdf.cell(ln=0, h=5.0, align='L', w=25.0, txt='Servicio', border=0)
        pdf.line(150.0, 28.0, 150.0, 102.0)
        pdf.set_xy(160.0, 30.0)
        pdf.cell(ln=0, h=5.0, align='R', w=20.0, txt='Dimensión', border=0)
        pdf.line(15.0, 36.0, 195.0, 36.0)
        pdf.line(195.0, 28.0, 195.0, 102.0)
        pdf.set_font("Arial", "", size=10)
        pdf.set_xy(20.0, 38.0)
        pdf.cell(ln=0, h=5.0, align='L', w=5.0, txt=self.leasing_cliente.placa, border=0)
        pdf.set_xy(50.0, 38.0)
        pdf.cell(ln=0, h=5.0, align='L', w=25.0, txt=self.leasing_cliente.tipo, border=0)
        pdf.set_xy(90.0, 38.0)
        pdf.cell(ln=0, h=5.0, align='L', w=25.0, txt=self.leasing_cliente.operacion, border=0)
        pdf.set_xy(120.0, 38.0)
        pdf.cell(ln=0, h=5.0, align='L', w=25.0, txt=self.leasing_cliente.servicio, border=0)
        pdf.set_xy(155.0, 38.0)
        pdf.cell(ln=0, h=5.0, align='R', w=20.0, txt=self.leasing_cliente.dimension, border=0)
        pdf.set_line_width(0.0)
        pdf.line(15.0, 102.0, 195.0, 102.0)
        pdf.set_xy(20.0, 97.0)
        pdf.add_page()
        pdf.set_left_margin(25)
        pdf.set_font("Arial", size=12)
        pdf.image(nombreimagen, 5,5,195,180)
        pdf.include_js('print(true);')
        pdf.output(outfile)
        
        self.outfilepdf= "/uploaded_files/{nombrearchivo}"
        pdfdownload=f"{ROUTEAPI_PDF}{self.leasing_cliente.id}-{self.cliente_sesion.id}-{self.user_actual.username}" 
        self.limpiar_pantalla()
        return rx.redirect(pdfdownload, is_external=True)

    @rx.var
    def logged_in(self) -> bool:
        """Check if a user is logged in."""
        return self.users is not None
    



