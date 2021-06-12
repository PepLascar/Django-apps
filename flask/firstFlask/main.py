from flask import Flask, flash, render_template, redirect, url_for, request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__) #Instanciar Flask

app.secret_key = 'clave_flask'   #clave secreta

#Conexion DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

#CONTEXT PROCESSORS
@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

@app.route('/')
def index():

    edad = 101
    personas = ['Hugo','Paco','Luis']

    return render_template("index.html",
                            edad = edad,
                            personas = personas,
                            dato1 = "valor",
                            dato2 = "valor2",
                            lista = ["1","2","3"]
                            )


@app.route('/holamundo')  #ruta con parámetro
def holamundo():
    return render_template("holamundo.html")


@app.route('/informacion/')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<apellidos>')
def informacion(nombre=None, apellidos=None):

    texto = ""
    if nombre != None and apellidos != None:
        texto = f"{nombre} {apellidos}"  #pasando el parámetro a la url
    else:
        texto = nombre

    return render_template("informacion.html", texto=texto)   #pasando la variable hacia el template


@app.route('/contacto')
@app.route('/contacto/<redir>')
def contacto(redir = None):

    if redir is not None:
        return redirect(url_for('lenguajes'))
    return render_template("contacto.html")


@app.route('/lenguajes')
def lenguajes():
    return render_template("lenguajes.html")

@app.route('/crear-servicio', methods=['GET', 'POST'])   #HABILITAR LOS MÉTODOS GET/POST
def crear_servicio():
    if request.method == 'POST':

        servicio = request.form['servicio']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        # return f" {servicio} {modelo} {precio} {ciudad} "  ..para comprobar funcionamiento del POST

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)", (servicio,modelo,precio,ciudad))  #incorporacion de los inputs para la base
        # cursor.execute(f"INSERT INTO coches VALUES(NULL, 'Lambo', 'Gallardo', 100, 'Malloco')") primer ejemplo con insert fijo
        cursor.connection.commit() #guardar cambios

        flash('Has agregado un artículo correctamente!')

        return redirect(url_for('index'))
        
    return render_template('crear-servicio.html')

@app.route('/listado')
def listar():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches ORDER BY id DESC")
    servicios = cursor.fetchall()  #obtengo todos los elementos de la tabla
    cursor.close()

    return render_template('listado.html', servicios=servicios)

#buscar
@app.route('/coche/<coche_id>')
def coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id=%s", (coche_id))
    buscar = cursor.fetchall()  #obtengo todos los elementos de la tabla
    cursor.close()

    return render_template('coche.html', buscar=buscar[0])  #cambiar coche por buscar o producto


#eliminar
@app.route('/eliminar/<coche_id>')
def eliminar(coche_id):
    cursor = mysql.connection.cursor()
    #cursor.execute("DELETE FROM coches WHERE id=%s", (coche_id))
    cursor.execute(f"DELETE FROM coches WHERE id= {coche_id}")
    mysql.connection.commit() #guardar cambios realizados
    flash('El elemento ha sido eliminado')

    return redirect(url_for('listar'))


#ACTUALIZAR
@app.route('/editar/<coche_id>', methods=['GET', 'POST'])
def editar(coche_id):
    if request.method == 'POST':

        servicio = request.form['servicio']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE coches
            SET marca = %s,
                modelo = %s,
                precio = %s,
                ciudad = %s
            WHERE id = %s
        """, (servicio, modelo, precio, ciudad, coche_id))  #incorporacion de los inputs para la base

        cursor.connection.commit() #guardar cambios
        flash('Editado correctamente!')

        return redirect(url_for('listar'))

    cursor = mysql.connection.cursor()
    #cursor.execute("SELECT * FROM coches WHERE id= %s", (coche_id))
    cursor.execute(f"SELECT * FROM coches WHERE id = {coche_id}")
    buscar = cursor.fetchall()
    cursor.close()

    return render_template('crear-servicio.html', buscar=buscar[0])


if __name__ == '__main__':
    app.run(debug=True)
