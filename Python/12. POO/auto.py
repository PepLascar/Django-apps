#CONSTRUCTOR

class Auto:
    # A t r i b u t o s / características de la clase
    color     = "Rojo"
    marca     = "Suzuki"
    modelo    = "Swift"
    velocidad = 100
    motor     = 1.5
    hp        = 115

    soy_publico   = "Soy un atributo PÚBLICO"
    __soy_privado = "Soy un atributo PRIVADO"

    # Constructor paramétrico (es un método). Cuando cree un objeto estas propiedades van a inicializarce.
    def __init__(self, color, marca, modelo, velocidad, motor, hp ):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.motor = motor
        self.hp = hp


    # Métodos, acciones o funcionalidades de la clase.
    # Modificar la propiedad acelerar de la clase (self)
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def setHp(self, hp):
        self.hp = hp

    def getHp(self):
        return self.hp

    def getPrivado(self):
        return self.__soy_privado

# Método para obtener toda la información del objeto
    def getInfo(self):
        info = "---- Información del auto ----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Hp: " + str(self.getHp())
        info += "\n"
        return info



    #fin de la clase y sus métodos