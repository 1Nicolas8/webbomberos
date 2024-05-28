#!/usr/bin/python3
import cgi
import sqlite3
import subprocess

form = cgi.FieldStorage()

conn = sqlite3.connect('registro.db')
cursor = conn.cursor()

usuario = form.getvalue('usuario')
nombre = form.getvalue('nombre')
password = form.getvalue('password')
correo = form.getvalue('correo')
telefono = form.getvalue('telefono')

cursor.execute("SELECT * FROM usuarios WHERE usuario = ? OR correo = ?", (usuario, correo))
existe = cursor.fetchone()

if existe:
    print("Content-Type: text/html; charset=utf-8\n")
    print("<html><head><title>Error de registro</title></head>")
    print("<body>")
    print("<p>El usuario o el correo electrónico ya se encuentran en uso.</p>")
    print("<p>Será redirigido a la página principal en 5 segundos...</p>")
    print("<meta http-equiv='refresh' content='5; url=index.html'>")
    print("</body></html>")
else:
    cursor.execute("INSERT INTO usuarios (usuario, nombre, password, correo, telefono, es_bombero) VALUES (?, ?, ?, ?, ?, 0)",
               (usuario, nombre, password, correo, telefono))
    conn.commit()

    print("Status: 303 See Other")
    print("Location: index.html")
    print("")

    subprocess.run(["python3", "confirmacion.py", correo, nombre])

conn.close()
