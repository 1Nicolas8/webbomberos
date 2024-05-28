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
print("<style>")
print("body {")
print("    font-family: Arial, sans-serif;")
print("    margin: 0;")
print("    padding: 0;")
print("    background-color: #f2f2f2;")
print("}")
print(".container {")
print("    max-width: 800px;")
print("    margin: 50px auto;")
print("    padding: 20px;")
print("    background-color: #fff;")
print("    border-radius: 10px;")
print("    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);")
print("}")
print("h1 {")
print("    color: #333;")
print("}")
print("p {")
print("    color: #666;")
print("}")
print("</style>")
print("</head>")
print("<body>")

conn = sqlite3.connect('registro.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO emergencias (usuario_id, descripcion, ubicacion) VALUES (?, ?, ?)",
               (usuario_id, descripcion, ubicacion))
conn.commit()

print("<div class='container'>")
print("<h1>Emergencia Reportada Exitosamente</h1>")
print("<p><strong>Descripción:</strong> " + descripcion + "</p>")
print("<p><strong>Ubicación:</strong> " + ubicacion + "</p>")
print("</div>")

print("</body>")
print("</html>")

conn.close()
