#!/usr/bin/python3
import cgi
import sqlite3

form = cgi.FieldStorage()
descripcion = form.getvalue('descripcion')
usuario_id = form.getvalue('usuario_id')
ubicacion = form.getvalue('ubicacion')

print("Content-type:text/html; charset=utf-8\n")
print("<html>")
print("<head>")
print("<title>Emergencia Reportada</title>")
print("</head>")
print("<body>")

conn = sqlite3.connect('registro.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO emergencias (usuario_id, descripcion, ubicacion) VALUES (?, ?, ?)",
               (usuario_id, descripcion, ubicacion))
conn.commit()

print("<h1>Emergencia Reportada Exitosamente</h1>")
print("<p>Descripción:", descripcion, "</p>")
print("<p>Ubicación:", ubicacion, "</p>")

print("</body>")
print("</html>")

conn.close()
