#!/usr/bin/python3
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import sys

load_dotenv()

# Obtener el correo electrónico y el nombre de usuario de los argumentos de la línea de comandos
correo_destinatario = sys.argv[1]
nombre_usuario = sys.argv[2]

# Configurar el correo electrónico
email_sender = "upcbomberitos@gmail.com"
password = "irqbalwcdgjixeik"
subject = "Responda triple hpta"
body = f"""
Estimado/a {nombre_usuario},

¡Saludos desde el equipo de la página de Bomberos!

Hemos recibido una solicitud para verificar tu cuenta en nuestro sitio web. Para completar el proceso de verificación y tener acceso completo a todas las funciones de la página, te pedimos que hagas clic en el enlace de abajo:

[Enlace de Verificación]

Si no has solicitado esta verificación o crees que has recibido este correo electrónico por error, por favor ignóralo.

¡Gracias por unirte a nuestra comunidad de Bomberos! Si tienes alguna pregunta o necesitas ayuda, no dudes en ponerte en contacto con nuestro equipo de soporte.

Atentamente,

Equipo de Bomberosupc
"""

# Crear el objeto de mensaje de correo electrónico
em = EmailMessage()
em["From"] = email_sender
em["To"] = correo_destinatario
em["Subject"] = subject
em.set_content(body)

# Configurar el contexto SSL
context = ssl.create_default_context()

# Enviar el correo electrónico
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, correo_destinatario, em.as_string())
