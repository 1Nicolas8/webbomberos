#!/usr/bin/python3
import cgi, cgitb
import sqlite3

conn = sqlite3.connect('fi.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
user_id = form.getvalue('user_id')
name = form.getvalue('name')
user = form.getvalue('user')
email = form.getvalue('email')
password = form.getvalue('password')
is_admin = form.getvalue('is_admin')

if user_id and name and user and email and password:
    try:
        is_admin_value = 1 if is_admin else 0
        cursor.execute("UPDATE TUTORIAS SET NAME = ?, USER = ?, EMAIL = ?, PASSWORD = ?, IS_ADMIN = ? WHERE ID = ?",
                       (name, user, email, password, is_admin_value, user_id))
        conn.commit()
        print("Content-type:text/html charset=utf-8\n")
        print("<html><head><title>Usuario Actualizado</title></head><body>")
        print("<h2>El usuario con ID {} ha sido actualizado exitosamente.</h2>".format(user_id))
        print("</body></html>")
    except sqlite3.Error as e:
        print("Content-type:text/html charset=utf-8\n")
        print("<html><head><title>Error</title></head><body>")
        print("<h2>Error al actualizar el usuario:</h2>")
        print("<p>{}</p>".format(str(e)))
        print("</body></html>")
else:
    print("Content-type:text/html charset=utf-8\n")
    print("<html><head><title>Error</title></head><body>")
    print("<h2>Faltan datos para actualizar el usuario.</h2>")
    print("</body></html>")

conn.close()
