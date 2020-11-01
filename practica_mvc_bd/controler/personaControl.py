from model.Alumno import Alumno

class controlPersona:

    def __init__(self):
        pass



    def CrearRegistro(self,lista):
        self.enlace = Alumno(lista[0],lista[1],lista[2],lista[3],lista[4])
        self.enlace.setMatricula(lista[5],lista[6],lista[7])
        self.enlace.insertarAlumnos()


    def LeerRegistro(self):
        pass

    def ActualizarRegistro(self,codigo):
        pass
    def EliminarRegistro(self,codigo):
        pass