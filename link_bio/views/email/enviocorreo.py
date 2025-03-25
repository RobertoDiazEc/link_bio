import reflex as rx
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailState(rx.State):
    email_status: str = ""

    def send_email(self, form_data: dict):
        try:
            # Configuración del servidor SMTP
            smtp_server = "smtp.gmail.com"
            port = 587
            sender_email = "tu_correo@gmail.com"
            password = "tu_contraseña"

            # Crear mensaje
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = form_data["to_email"]
            message["Subject"] = form_data["subject"]

            # Agregar cuerpo del mensaje
            body = form_data["message"]
            message.attach(MIMEText(body, "plain"))

            # Iniciar servidor y enviar
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(sender_email, password)
            text = message.as_string()
            server.sendmail(sender_email, form_data["to_email"], text)
            server.quit()
            
            self.email_status = "Correo enviado exitosamente"
        except Exception as e:
            self.email_status = f"Error al enviar correo: {str(e)}"

def email_form_envio():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Destinatario",
                    name="to_email",
                ),
                rx.input(
                    placeholder="Asunto",
                    name="subject",
                ),
                rx.text_area(
                    placeholder="Mensaje",
                    name="message",
                ),
                rx.button("Enviar", type="submit"),
                spacing="4",
            ),
            on_submit=EmailState.send_email,
        ),
        rx.text(EmailState.email_status),
        spacing="4",
    )
