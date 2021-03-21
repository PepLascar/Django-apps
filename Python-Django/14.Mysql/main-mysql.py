import mysql.connector

#Conexión

database = mysql.connector.connect(
    host      = "localhost",
    user      = "root",
    passwd    = "1234",
    database  = "base_python"

)
"""
# Comprobar conexión
print(database)

cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS base_python")

cursor.execute("SHOW DATABASES")
for i in cursor:
    print(i)
"""
#CREANDO EL CURSOR
cursor = database.cursor(buffered=True)
cursor.execute ("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id INTEGER(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")

cursor.execute("SHOW TABLES")
for i in cursor:
    print(i)

"""
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Suzuki', 'SwiftSport', 1000)")
database.commit()

#Create tubla con varios datos
autos = [
    ('Ssanyong','Actyon',1000),
    ('Toyota','Yaris',2000),
    ('KIA','rio',3000),
    ('MG3','MG',4000)
]


cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", autos)
database.commit()
"""
# M O S T R A R
cursor.execute("SELECT * FROM vehiculos where precio <= 3000 and marca = 'suzuki'")
#con esto voy a sacar los datos que obtuvo el cursor
result = cursor.fetchall()   #o se puede usar fetchone

for i in result:
    print(f'Id: {i[1], i[3]}') #el [1] es la finla que quiero obtener de la tabla/tupla

print("-------------")

cursor.execute("SELECT * FROM vehiculos") #Obteniendo solo 1
auto = cursor.fetchone()
print(auto)

#B O R R A R 
print("-----------")
cursor.execute("DELETE FROM vehiculos where marca = 'Ssanyong'")
database.commit()

#Mostrar que se ha borrado
print(cursor.rowcount, " elemento borrado!")


# A C T U A L I Z A R
cursor.execute("UPDATE vehiculos SET modelo = '888' where marca = 'KIA' ")
database.commit()

#Finalmente mostramos todo
cursor.execute("SELECT * FROM vehiculos")
mostrar = cursor.fetchall()

for i in mostrar:
    print(i)
