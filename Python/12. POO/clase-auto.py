import os
os.system("cls")
# Clase: molde para crear objetos de X tipo con características similares.
# contienen atributos (características) y métodos.

class Auto:
    # A t r i b u t o s / características de la clase
    color     = "Rojo"
    marca     = "Suzuki"
    modelo    = "Swift"
    velocidad = 100
    motor     = 1.5
    hp        = 115


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

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    #fin de la clase y sus métodos


auto = Auto()

# Usando setter
auto.setColor("Gris")
auto.setModelo("Swift")

# Crear objetos / Instanciar clase
print(  auto.marca, auto.getModelo(), auto.getColor()  )
# print(Auto.marca, Auto.color)  #Llamando atributos
print("Velocidad actual: ", auto.getVelocidad())

""" Estos son setter por que estoyt asignando
Auto.acelerar()
Auto.acelerar()
Auto.acelerar()
Auto.acelerar()
Auto.acelerar()
"""

auto.frenar()
auto.frenar()
print("Velocidad nueva: ", auto.getVelocidad())

auto2 = Auto()
auto2.setColor("Amarillo")
auto2.setModelo("Swift Sport")

print("\n--Auto 2--")
print( auto2.getModelo(), auto2.getColor() )
print(type(auto2))

