#!/usr/bin/python3
import cgi
import sqlite3

# Crear una instancia de FieldStorage
form = cgi.FieldStorage()

# Conectar a la base de datos
conn = sqlite3.connect('registro.db')
cursor = conn.cursor()

# Obtener los datos del formulario
usuario = form.getvalue('usuario')
nombre = form.getvalue('nombre')
password = form.getvalue('password')
correo = form.getvalue('correo')
telefono = form.getvalue('telefono')

# Verificar si el usuario o el correo ya existen en la base de datos
cursor.execute("SELECT * FROM usuarios WHERE usuario = ? OR correo = ?", (usuario, correo))
existe = cursor.fetchone()

if existe:
    # Mostrar un mensaje de error y redireccionar a index.html
    print("Content-Type: text/html; charset=utf-8\n")
    print("<html><head><title>Error de registro</title></head>")
    print("<body>")
    print("<p>El usuario o el correo electrónico ya existen en la base de datos.</p>")
    print("<p>Será redirigido a la página principal en 5 segundos...</p>")
    print("<meta http-equiv='refresh' content='5; url=index.html'>")
    print("</body></html>")
else:
    # Insertar los datos en la tabla usuarios
    cursor.execute("INSERT INTO usuarios (usuario, nombre, password, correo, telefono) VALUES (?, ?, ?, ?, ?)",
                   (usuario, nombre, password, correo, telefono))
    conn.commit()

    # Redireccionar a index.html después de un registro exitoso
    print("Status: 303 See Other")
    print("Location: index.html")
    print("")

# Cerrar la conexión
conn.close()