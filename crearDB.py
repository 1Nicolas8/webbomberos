#!/usr/bin/python3
import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect('registro.db')
cursor = conn.cursor()

conn.execute("DROP TABLE IF EXISTS usuarios")

# Crear la tabla usuarios
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   usuario TEXT NOT NULL UNIQUE,
                   nombre TEXT NOT NULL,
                   password TEXT NOT NULL,
                   correo TEXT NOT NULL UNIQUE,
                   telefono TEXT NOT NULL)''')

print("Tabla usuarios creada exitosamente")

# Cerrar la conexión
conn.close()