import random

class Caballo:
    def __init__(self, nombre, favorito = False):
        self.nombre = nombre
        self.posicion = 0
        self.favorito = favorito
      
    def __str__(self):
        return self.nombre
    
    def avanzar(self):
        if self.favorito:
            self.posicion += random.randint(1, 6)
        else:
            self.posicion += random.randint(1, 5)
      
# s = Caballo("Sally", True)

# print(s)
# while s.posicion < 20:
#     print(s.posicion)
#     s.avanzar()