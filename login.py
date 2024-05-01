#!/usr/bin/python3
import cgi, cgitb
import sqlite3
import base64

form = cgi.FieldStorage()
correo = form.getvalue('email')
password = form.getvalue('paxx')

print("Content-type:text/html charset=utf-8\n")
print("<html><head><title>Ingreso al Sistema</title></head><body>")

conn = sqlite3.connect('fi.db')
sql0 = "SELECT EMAIL, PASSWORD, IS_ADMIN FROM TUTORIAS WHERE EMAIL = '%s'" % correo
cursor = conn.cursor()
cursor.execute(sql0)
conn.commit()
retorno_datos = cursor.fetchone()

if retorno_datos:
    correo_db, password_db, is_admin = retorno_datos
    if is_admin == 1:
        if password_db == password:
            print("<h2>Administracion de cuentas creadas</h2>")
            sql_users = "SELECT ID, NAME, USER, EMAIL, IS_ADMIN FROM TUTORIAS WHERE EMAIL != '%s'" % correo
            cursor.execute(sql_users)
            users_data = cursor.fetchall()

            print("<table border='1'>")
            print("<tr><th>ID</th><th>Nombre</th><th>Usuario</th><th>Correo</th><th>Admin</th><th>Acciones</th></tr>")
            for user in users_data:
                print("<tr>")
                for value in user[:-1]:
                    print("<td>{}</td>".format(value))
                print("<td>{}</td>".format("Si" if user[-1] else "No"))
                print("<td>")
                print("<form action='/editar_usuario.py' method='post'>")
                print("<input type='hidden' name='user_id' value='{}'>".format(user[0]))
                print("<input type='submit' value='Editar'>")
                print("</form>")
                print("<form action='/eliminar_usuario.py' method='post'>")
                print("<input type='hidden' name='user_id' value='{}'>".format(user[0]))
                print("<input type='submit' value='Eliminar'>")
                print("</form>")
                print("</td>")
                print("</tr>")
            print("</table>")
        else:
            print("<h2>password incorrecto para el usuario administrador</h2>")
    else:
        if retorno_datos[1]:
            if retorno_datos[1] == password:
                print("<h2>Bienvenido al Sistema</h2>")
                sql2 = "SELECT NAME, IMAGEN FROM TUTORIAS WHERE EMAIL = '%s'" % correo
                cursor.execute(sql2)
                conn.commit()
                resultado = cursor.fetchone()
                nombres = resultado[0]
                imagen_codificada = resultado[1]

                if imagen_codificada:
                    imagen_decodificada = base64.b64decode(imagen_codificada)
                    print("<img src='data:image/jpeg;base64,%s'>" % imagen_codificada.decode('utf-8'))

                print("<h2>Estimado", nombres, "le agradecemos su ingreso</h2>")
                print("<h2>Ahora puede comenzar a elegir su tutoria </h2>")
                print("</body></html>")
            else:
                print("<h2>Su password no es correcto</h2>")
                print("<h2>Vuelva a intentarlo</h2>")
                print("</body></html>")
        else:
            print("<h2>Su cuenta no tiene password asignado</h2>")
            print("<h2>Vuelva a intentar registrarse</h2>")
            print("</body></html>")
else:
    retorno = "None"
    print("<h2>Lo sentimos Usted no esta registrado en nuestro sistema por favor registrese</h2>")
    print("</body></html>")

conn.close()
