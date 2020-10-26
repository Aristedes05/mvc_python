import pymysql

class Conexion:

    def __init__(self):
        self.servidor="localhost"
        self.bd="estudiante"
        self.user="root"
        self.clave=""

    def conectar(self):
        try:
            self.conexion = pymysql.connect(self.servidor,self.user,self.clave,self.bd)
            self.cn = self.conexion.cursor()
            print("La conexión se realizo exitosamente")

        except Exception as e:
            print("Error",e)
