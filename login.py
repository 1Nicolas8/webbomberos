#!/usr/bin/python3
import cgi
import cgitb
import sqlite3

form = cgi.FieldStorage()
usuario = form.getvalue('username')
password = form.getvalue('password')

print("Content-type:text/html;charset=utf-8\n")
print("<html><head><title>Ingreso al Sistema</title>")
print("<style>")
print("""
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f2f2f2;
}

#container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    color: #333;
}

table {
    width: 100%;
    border-collapse: collapse;
}

table, th, td {
    border: 1px solid #ddd;
}

th, td {
    padding: 8px;
    text-align: left;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

form {
    margin-top: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"] {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #45a049;
}

.error {
    color: red;
}
""")
print("</style></head><body>")

conn = sqlite3.connect('registro.db')
cursor = conn.cursor()

# Consulta para obtener los datos del usuario
sql_usuario = "SELECT usuario, password, es_bombero, id FROM usuarios WHERE usuario = ?"
cursor.execute(sql_usuario, (usuario,))
retorno_datos = cursor.fetchone()

if retorno_datos:
    usuario_db, password_db, es_bombero, usuario_id = retorno_datos
    if es_bombero:
        if password_db == password:
            print("<div id='container'>")
            print("<h2>Administración de emergencias registradas</h2>")
            # Consulta para obtener los datos de emergencias
            sql_emergencias = "SELECT id, descripcion, ubicacion, fecha, usuario_id FROM emergencias"
            cursor.execute(sql_emergencias)
            emergencias_data = cursor.fetchall()
            print("<table>")
            print("<tr><th>ID</th><th>Descripción</th><th>Ubicación</th><th>Fecha</th><th>Nombre</th><th>Usuario</th><th>Teléfono</th></tr>")
            for emergencia in emergencias_data:
                emergencia_id, descripcion, ubicacion, fecha, usuario_id = emergencia
                # Consulta para obtener los datos del usuario de la emergencia actual
                sql_datos_usuario = "SELECT nombre, usuario, telefono FROM usuarios WHERE id = ?"
                cursor.execute(sql_datos_usuario, (usuario_id,))
                datos_usuario = cursor.fetchone()
                if datos_usuario:
                    nombre, nombre_usuario, telefono = datos_usuario
                    print("<tr>")
                    print("<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>".format(emergencia_id, descripcion, ubicacion, fecha, nombre, nombre_usuario, telefono))
                    print("</tr>")
            print("</table>")
            print("</div>")
        else:
            print("<div id='container'><h2 class='error'>Contraseña incorrecta para el usuario bombero</h2></div>")
    else:
        if password_db == password:
            print("<div id='container'>")
            print("<h2>Bienvenido al Sistema</h2>")
            print("<h2>Puede registrar una nueva emergencia</h2>")
            print("<form action='/registrar_emergencia.py' method='post'>")
            print("<label for='descripcion'>Descripción:</label>")
            print("<input type='text' id='descripcion' name='descripcion' required>")
            print("<input type='hidden' id='ubicacion' name='ubicacion'>")
            print("<input type='hidden' name='usuario_id' value='{}'>".format(usuario_id))
            print("<input type='submit' value='Enviar'>")
            print("</form>")
            print("<script>")
            print("function getLocation() {")
            print("  if (navigator.geolocation) {")
            print("    navigator.geolocation.getCurrentPosition(function(position) {")
            print("      var latitude = position.coords.latitude;")
            print("      var longitude = position.coords.longitude;")
            print("      document.getElementById('ubicacion').value = 'Latitud: ' + latitude + ', Longitud: ' + longitude;")
            print("    });")
            print("  } else {")
            print("    alert('La geolocalización no es compatible en este dispositivo.');")
            print("  }")
            print("}")
            print("getLocation();")
            print("</script>")
            print("</div>")
        else:
            print("<div id='container'><h2 class='error'>Contraseña incorrecta para el usuario</h2></div>")
else:
    print("<div id='container'><h2 class='error'>Usuario no encontrado</h2></div>")

print("</body></html>")
conn.close()
