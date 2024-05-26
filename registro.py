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

# Insertar los datos en la tabla usuarios
cursor.execute("INSERT INTO usuarios (usuario, nombre, password, correo, telefono) VALUES (?, ?, ?, ?, ?)",
               (usuario, nombre, password, correo, telefono))
conn.commit()

# Cerrar la conexión
conn.close()
