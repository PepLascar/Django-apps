import mysql.connector


def conectar():
    database = mysql.connector.connect(
        host      = "localhost",
        user      = "root",
        passwd    = "1234",
        database  = "proyecto_1",
        port      = 3306
    )

    cursor = database.cursor(buffered=True)

    return [database,cursor]