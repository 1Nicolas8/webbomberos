#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sqlite3

# Activar la visualización de errores
cgitb.enable()

# Crear instancia para almacenar los datos del formulario
form = cgi.FieldStorage()

# Obtener los datos del formulario
usuario = form.getvalue('usuario')
nombre = form.getvalue('nombre')
password = form.getvalue('password')
password2 = form.getvalue('password2')
correo = form.getvalue('correo')
telefono = form.getvalue('telefono')
terminos = form.getvalue('terminos')

# Validar los datos (puedes agregar más validaciones según sea necesario)
if not usuario or not nombre or not password or not password2 or not correo or not telefono or not terminos:
    print("Content-type:text/html\r\n\r\n")
    print("<html><head><title>Error en el formulario</title></head>")
    print("<body><h1>Error: Todos los campos son obligatorios.</h1></body></html>")
else:
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('registro.db')
    c = conn.cursor()

    # Verificar si el correo ya está registrado
    c.execute("SELECT * FROM usuarios WHERE correo = ?", (correo,))
    resultado = c.fetchone()

    if resultado:
        print("Content-type:text/html\r\n\r\n")
        print("<html><head><title>Error en el formulario</title></head>")
        print("<body><h1>Error: El correo electrónico ya está registrado.</h1></body></html>")
    else:
        # Insertar los datos en la tabla "usuarios"
        c.execute("INSERT INTO usuarios (usuario, nombre, password, correo, telefono) VALUES (?, ?, ?, ?, ?)",
                  (usuario, nombre, password, correo, telefono))
        conn.commit()
        print("Content-type:text/html\r\n\r\n")
        print("<html><head><title>Registro exitoso</title></head>")
        print("<body><h1>Registro exitoso</h1></body></html>")

    conn.close()