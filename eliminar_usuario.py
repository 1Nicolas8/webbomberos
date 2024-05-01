#!/usr/bin/python3
import cgi, cgitb
import sqlite3

conn = sqlite3.connect('fi.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
user_id = form.getvalue('user_id')

conn = sqlite3.connect('fi.db')
sql0 = "SELECT EMAIL, IS_ADMIN FROM TUTORIAS WHERE ID = '%s'" % user_id
cursor=conn.cursor()
cursor.execute(sql0)
retorno_datos=cursor.fetchone()

if user_id:
    if user_id == "1" and retorno_datos[1] == 1:
        print("Content-type:text/html charset=utf-8\n")
        print("<html><head><title>Eliminacion de Usuario</title></head><body>")
        print("<h2>No se puede eliminar el usuario administrador principal</h2>")
        print("</body></html>")
    else:
        try:
            cursor.execute("DELETE FROM TUTORIAS WHERE ID = ?", (user_id,))
            conn.commit()
            print("Content-type:text/html charset=utf-8\n")
            print("<html><head><title>Eliminacion de Usuario</title></head><body>")
            print("<h2>El usuario con ID {} ha sido eliminado exitosamente.</h2>".format(user_id))
            print("</body></html>")
        except sqlite3.Error as e:
            print("Content-type:text/html charset=utf-8\n")
            print("<html><head><title>Error</title></head><body>")
            print("<h2>Error al eliminar el usuario:</h2>")
            print("<p>{}</p>".format(str(e)))
            print("</body></html>")
else:
    print("Content-type:text/html charset=utf-8\n")
    print("<html><head><title>Error</title></head><body>")
    print("<h2>No se proporciono un ID de usuario valido.</h2>")
    print("</body></html>")

conn.close()
