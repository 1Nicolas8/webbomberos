#!/usr/bin/python3
import sqlite3
import os

# Eliminar la base de datos actual si existe
if os.path.exists('registro.db'):
    os.remove('registro.db')

# Conectar a una nueva base de datos (se crea si no existe)
conn = sqlite3.connect('registro.db')
cursor = conn.cursor()

# Crear la tabla usuarios
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   usuario TEXT NOT NULL UNIQUE,
                   nombre TEXT NOT NULL,
                   password TEXT NOT NULL,
                   correo TEXT NOT NULL UNIQUE,
                   telefono TEXT NOT NULL,
                   es_bombero BOOLEAN DEFAULT 0)''')

# Crear la tabla emergencias
cursor.execute('''CREATE TABLE IF NOT EXISTS emergencias
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   usuario_id INTEGER NOT NULL,
                   descripcion TEXT NOT NULL,
                   ubicacion TEXT NOT NULL,
                   fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
                   FOREIGN KEY (usuario_id) REFERENCES usuarios(id))''')

print("Tablas creadas exitosamente")

# Cerrar la conexión
conn.close()
