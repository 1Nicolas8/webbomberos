#!/usr/bin/python3
#importamos el modulo para manejar el CGI
import cgi, cgitb
import sqlite3
#Creamos instancia para almacenar
form=cgi.FieldStorage()
#Obtener los datos del formulario
correo=form.getvalue('email')
password=form.getvalue('pass')
print "Content-type:text/html charset=utf-8\n"
print ("<html><head><title>Ingreso al Sistema</title></head><body>")
conn = sqlite3.connect('fi.db')
sql0 = "SELECT EMAIL FROM TUTORIAS WHERE EMAIL = '%s'" % correo
sql1 = "SELECT PASSWORD FROM TUTORIAS WHERE EMAIL = '%s'" % correo
cursor=conn.cursor()
cursor.execute(sql0)
conn.commit()
retorno_correo=cursor.fetchone()
if retorno_correo:
	cursor.execute(sql1)
	conn.commit()
	retorno_pass=cursor.fetchone()
	if retorno_pass:
		if retorno_pass[0]==password:
			print("<h2>Bienvenido al Sistema</h2>")
			sql2 = "SELECT NAME FROM TUTORIAS WHERE EMAIL = '%s'" % correo
			cursor.execute(sql2)
			conn.commit()
			resultado_name=cursor.fetchone()
			nombres=resultado_name[0]
			print("<h2>Estimado %s le agradecemos su ingreso</h2>") % nombres 
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
	retorno="None"
	#print retorno
	print ("<h2>Lo sentimos Usted no esta registrado en nuestro sistema por favor registrese</h2>")
 	print("</body></html>")
conn.close()



