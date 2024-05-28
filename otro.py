#!/usr/bin/python3
import sqlite3
conn = sqlite3.connect('fi.db')
print ("Se conecto bien")
id=23
nombre='luis'
usuario='lfeli99'
correo='lfeli99@gmail.com'
password='dkdkd'
sql = "INSERT INTO TUTORIAS VALUES('%d','%s','%s','%s','%s')" % (id, nombre, usuario, correo, password)
conn.execute(sql);
print("almaceno los registros")
conn.commit()
conn.close()
