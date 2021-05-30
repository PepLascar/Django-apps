import mysql.connector

database = mysql.connector.connect(
    host      = "localhost",
    user      = "root",
    passwd    = "1234",
    database  = "proyecto_1",
    port      = 3306
)

# Comprobar conexión
print(database)

cursor = database.cursor(buffered=True)
cursor.execute("CREATE DATABASE IF NOT EXISTS proyecto_1")

cursor.execute("SHOW DATABASES")
for i in cursor:
    print(i)

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id int(20) auto_increment NOT NULL,
    nombre varchar(60),
    apellidos varchar(80),
    mail varchar(40) NOT NULL,
    password varchar(30) NOT NULL,
    fecha date NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_mail UNIQUE (mail)            
)ENGINE=InnoDb;""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS notas(
    id int(20) auto_increment NOT NULL,
    usuario_id int(25) NOT NULL,
    titulo varchar(100) NOT NULL,
    descripcion text,
    fecha date NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY (id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;""")