class Hipodromo:
    def __init__(self,nombre,filas,metros,ornamento):
        self.nombre = nombre
        self.filas = filas
        self.metros = metros
        self.ornamento = ornamento
        self.pista = []
        for i in range(filas):
            self.pista.append([ornamento]*metros)

    def poner_caballo(self, caballo, fila, posicion):
        self.pista[fila][posicion] = caballo

    def mostrar(self):
        print(f"   HIPODROMO DE {self.nombre}".center(self.metros))
        print(" ||SALIDA" + ("=" *(self.metros-1) + "||META"))
        for i in range(self.filas):
            print(" ", end=" ")
            for j in range(self.metros):
                print(self.pista[i][j], end=" ")
            print()

# h = Hipodromo("La Montaña", 8, 40, "-")
# h.mostrar()