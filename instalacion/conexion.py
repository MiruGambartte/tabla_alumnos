import mysql.connector
from mysql.connector import Error
class DataBase:
    try:
        conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        db='rodaja'
        )
    
        if conexion.is_connected():
            print("Conexión exitosa")
            cursor=conexion.cursor()
            nombre=input("ingrese el nombre del usuario: ")
            DNI=input("ingrese el DNI del usuario: ")
            domicilio=input("ingrese el domicilio del usuario: ")
            email=input("ingrese el email del usuario: ")
            sentencia="INSERT INTO alumno (nombre,dni,domicilio,email) VALUES (%s,%s,%s,%s)"
            valor=(nombre, DNI, domicilio, email)
            
            cursor.execute(sentencia, valor)
            conexion.commit()
            print("registro realizado con exito")
    except Error as ex:
        print("Error durante la conexion:",ex)
    finally:
        if conexion.is_connected():
            conexion.close()
            print("La conexión ha finalizado")

