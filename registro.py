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
    print("<p>El usuario o el correo electrónico ya se encuentran en uso.</p>")
    print("<p><a href='index.html'>Volver a la página principal</a></p>")
    print("</body></html>")
else:
    # Insertar los datos en la tabla usuarios
    cursor.execute("INSERT INTO usuarios (usuario, nombre, password, correo, telefono) VALUES (?, ?, ?, ?, ?)",
                   (usuario, nombre, password, correo, telefono))
    conn.commit()

    # Redireccionar a index.html después de un registro exitoso
    print("Content-Type: text/html; charset=utf-8\n")
    print("<html><head><title>Registro exitoso</title></head>")
    print("<body>")
    print("<p>Registro exitoso.</p>")
    print("<p><a href='index.html'>Volver a la página principal</a></p>")
    print("</body></html>")

# Cerrar la conexión
conn.close()