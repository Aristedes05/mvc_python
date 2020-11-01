class Persona:

    def __init__(self,nombre,apellidos,edad,dni,sexo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.dni = dni
        self.sexo = sexo


    def setNombre(self,nombre):
        self.nombre = nombre
    def setApellidos(self,apellidos):
        self.apellidos = apellidos
    def setEdad(self,edad):
        self.edad = edad
    def setDNI(self,dni):
        self.dni = dni
    def setSexo(self,sexo):
        self.sexo = sexo


    
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getEdad(self):
        return self.edad
    def getDNI(self):
        return self.dni
    def getSexo(self):
        return self.sexo
