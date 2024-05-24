#!/usr/bin/python3
#importamos el modulo para manejar el CGI
import cgi, cgitb
import sqlite3
#Creamos instancia para almacenar
form=cgi.FieldStorage()
#Obtener los datos del formulario
id=form.getvalue('id')
nombre=form.getvalue('name')
usuario=form.getvalue('user')
correo=form.getvalue('email')
password=form.getvalue('pass')
print "Content-type:text/html\n"
print ("<html><head><title>Respuesta del formulario</title></head><body>")
print ("<h2>el ID es: %s </h2>"% id)
print ("<h2>El nombre es: %s </h2>"% nombre)
print ("<h2>El usuario es: %s </h2>"% usuario)
print ("<h2>El correo  es: %s </h2>"% correo)
print ("<h2>El password es: %s </h2>"% password)
print ("</body></html>")
for i in range (0,5):
	print ("<br>HOLA")
conn = sqlite3.connect('fi.db')
print ("<br>Se conecto bien")
sql = "INSERT INTO TUTORIAS VALUES('%s','%s','%s','%s','%s')" % (id, nombre, usuario, correo, password)
conn.execute(sql);
print("almaceno los registros")
conn.commit()
conn.close()

