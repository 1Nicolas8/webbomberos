#!/usr/bin/python3
#importamos el módulo para manejar el CGI
import cgi, cgitb
import sqlite3
import base64

# Activar la visualización de errores
cgitb.enable()

# Creamos instancia para almacenar
form = cgi.FieldStorage()

# Obtener los datos del formulario
id = form.getvalue('id')
nombre = form.getvalue('name')
usuario = form.getvalue('user')
correo = form.getvalue('email')
password = form.getvalue('pass')
imagen = form['imagen']
imagen_contenido = imagen.file.read()
imagen_codificada = base64.b64encode(imagen_contenido)

print("Content-type:text/html;charset=utf-8\n")
print("<html><head><title>Respuesta del Registro</title></head><body>")
print("<h2>Gracias por usar nuestra plataforma</h2>")
conn = sqlite3.connect('fi.db')
cursor = conn.cursor()

# Comprobar si el correo y usuario ya está registrado
sql0 = "SELECT ID FROM TUTORIAS WHERE ID = ?"
cursor.execute(sql0, (id,))
retorno_id = cursor.fetchone()

if retorno_id:
    print("<h2>Lo sentimos, el id que intentas ingresar ya está registrado. Por favor, envía un correo a nuestro administrador a ttt@ttt.rr</h2>")
    print("<h2>Agradecemos tu paciencia.</h2>")
else:
	sql1 = "SELECT EMAIL FROM TUTORIAS WHERE EMAIL = ?"
	cursor.execute(sql0, (correo,))
	retorno = cursor.fetchone()

	if retorno:
	    print("<h2>Lo sentimos, el usuario que intentas ingresar ya está registrado. Por favor, envía un correo a nuestro administrador a ttt@ttt.rr</h2>")
	    print("<h2>Agradecemos tu paciencia.</h2>")
	else:
	    # Insertar datos en la base de datos
	    sql1 = "INSERT INTO TUTORIAS VALUES (?, ?, ?, ?, ?, ?, ?)"
	    cursor.execute(sql1, (id, nombre, usuario, correo, password, imagen_codificada, 0))
	    conn.commit()
	    print("<h2>Su registro fue exitoso</h2>")
	    print("<h2>Ahora ingresa a nuestra plataforma regresando a la página principal.</h2>") 

print("</body></html>")
conn.close()
