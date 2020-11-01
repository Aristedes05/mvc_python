from .Persona import Persona
from .Conexion import Conexion


class Alumno(Persona):


    codigo = ""
    carrera = ""
    ciclo =""

    def __init__(self,nombre,apellidos,edad,dni,sexo):
        Persona.__init__(self,nombre,apellidos,edad,dni,sexo)

    def setMatricula(self,codigo,carrera,ciclo):
        self.codigo = codigo
        self.carrera = carrera
        self.ciclo = ciclo

    def setCodigo(self,codigo):
        self.codigo = codigo
    def setCarrera(self,carrera):
        self.carrera = carrera
    def setCiclo(self,ciclo):
        self.ciclo = ciclo

    def getCodigo(self):
        return self.codigo
    def getCarrera(self):
        return self.carrera
    def getCiclo(self):
        return self.ciclo



# crear alumnos
    def insertarAlumnos(self):
        conecta = Conexion()
        conecta.conectar()

        print("Registro creado")


# leer alumnos
    def leerAlumnos(self):
        pass

# actualizar alumnos

    def actualizarAlumnos(self):
        pass

# eliminar alumnos
    def eliminarAlumnos(self):
        pass

