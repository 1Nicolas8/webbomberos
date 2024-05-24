#!/usr/bin/python3
#importamos el modulo para manejar el CGI
import cgi, cgitb
import sqlite3
#Creamos instancia para almacenar
form=cgi.FieldStorage()
#Obtener los datos del formulario
id=22
nombre='andres'
usuario='lfeli99'
correo='lfeli99@gmail.com'
password='pass'
conn = sqlite3.connect('fi.db')
sql0 = "SELECT EMAIL FROM TUTORIAS WHERE EMAIL = '%s'" % correo
cursor=conn.cursor()
cursor.execute(sql0)
retorno=cursor.fetchone()
if retorno:
	print ("<h2>Lo sentimos el usuario que intentas ingresar ya esta registrado, su correo figura en nuestros datos</h2>")
else:
	retorno="None"
	#print retorno
	sql1 = "INSERT INTO TUTORIAS VALUES('%s','%s','%s','%s','%s')" % (id, nombre, usuario, correo, password) 
	conn.execute(sql1);
	conn.commit()
	print ("<h2>Su Registro fue exitoso</h2>")
conn.close()


