# Herencia : Es la posibilidad de compartir atributos y métodos entre clases. Y que diferentes clases hereden de otras.
# Clase padre y clases hijas que hereden esos atributos y métodos.

class Persona:
 
    nombre = ""
    apellido = ""
    altura = ""
    edad = ""

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setAltura (self, altura):
        self.altura = altura
    
    def setEdad (self, edad):
        self.edad = edad

    def hablar(self):
        return "Hablando"
    
    def caminar(self):
        return "Caminando"
    
    def dormir(self):
        return "Durmiendo"

class Informatico(Persona): #Heredo de la clase padre los ATRIBUTOS de PERSONA
    """lenguajes
    experiencia"""
    def __init__(self):   #Constructor privado
        self.lenguajes = "HTML, DJANGO, JAVA, FLASK"
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Programando"

class TecnicoRedes(Informatico): #Esta clase tendría todas las características de Persona e -> Informático
    def __init__(self): #Constructor privado que solamente se pueden acceder desde esta propia clase
        super().__init__()  #Aquí se cargan los constructores que tiene la clase padre
        self.auditarRed = "experto"
        self.experienciaRedes = 8

    def auditoria(self):
        return "Auditando red"


    
