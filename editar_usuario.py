#!/usr/bin/python3
import cgi, cgitb
import sqlite3

conn = sqlite3.connect('fi.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
user_id = form.getvalue('user_id')

if user_id:
    try:
        # Obtener los datos actuales del usuario
        cursor.execute("SELECT NAME, USER, EMAIL, PASSWORD, IMAGEN, IS_ADMIN FROM TUTORIAS WHERE ID = ?", (user_id,))
        user_data = cursor.fetchone()

        print("Content-type:text/html charset=utf-8\n")
        print("<html><head><title>Editar Usuario</title></head><body>")
        print("<h2>Editar Usuario con ID {}</h2>".format(user_id))

        print("<form action='/guardar_usuario.py' method='post'>")
        print("<input type='hidden' name='user_id' value='{}'>".format(user_id))
        print("<label for='name'>Nombre:</label>")
        print("<input type='text' id='name' name='name' value='{}'>".format(user_data[0]))
        print("<br>")
        print("<label for='user'>Usuario:</label>")
        print("<input type='text' id='user' name='user' value='{}'>".format(user_data[1]))
        print("<br>")
        print("<label for='email'>Correo:</label>")
        print("<input type='email' id='email' name='email' value='{}'>".format(user_data[2]))
        print("<br>")
        print("<label for='password'>Password:</label>")
        print("<input type='password' id='password' name='password' value='{}'>".format(user_data[3]))
        print("<br>")
        print("<label for='is_admin'>Administrador:</label>")
        print("<input type='checkbox' id='is_admin' name='is_admin' {}>".format("checked" if user_data[5] else ""))
        print("<br>")
        print("<input type='submit' value='Guardar Cambios'>")
        print("</form>")

        print("</body></html>")
    except sqlite3.Error as e:
        print("Content-type:text/html charset=utf-8\n")
        print("<html><head><title>Error</title></head><body>")
        print("<h2>Error al obtener los datos del usuario:</h2>")
        print("<p>{}</p>".format(str(e)))
        print("</body></html>")
else:
    print("Content-type:text/html charset=utf-8\n")
    print("<html><head><title>Error</title></head><body>")
    print("<h2>No se proporciono un ID de usuario valido.</h2>")
    print("</body></html>")

conn.close()
