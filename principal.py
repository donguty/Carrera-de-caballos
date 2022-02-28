from caballo import Caballo
from hipodromo import Hipodromo
import time
import random
import os

def portada():
    print("--------------------------------------------------")
    print("    BIENVENIDO A LAS CARRERAS DE CABALLOS         ")
    print()
    print("        Elige un Hipódromo") 
    print()
    print("      1. Hipódromo de la Montaña")
    print("      2. Hipódromo de la Ciudad")
    print("      3. Hipódromo de la Zarzuela")
    print()
    opcion = ""
    while opcion not in ("1","2","3"):
        opcion = input("   --> ")
    return opcion

if __name__=="__main__":
    os.system("clear")
    opcion = portada()
    
    if opcion == "1":
        hipodromo = Hipodromo("La Montaña", 8, 40, "-")
    elif opcion == "2":
        hipodromo = Hipodromo("La Ciudad", 10, 45, ".")
    elif opcion=="3":
        hipodromo = Hipodromo("La Zarzuela", 6, 50, "_")
    
    nombres = ["p","r","s","t","u","v","w","x","y","z"]
    caballos = []
    for i in range(hipodromo.filas):
        favorito = random.choice([True, False])
        caballo = Caballo(nombres[i], favorito)
        caballos.append(caballo)
        
    for i in range(hipodromo.filas):
        hipodromo.poner_caballo(caballos[i], i, caballos[i].posicion)
        
    os.system("clear")
    
    hipodromo.mostrar()
    
    print()
    print("  Los caballos favoritos son:", end=" ")
    for caballo in caballos:
        if caballo.favorito:
            print(f" {caballo}", end=" ")
    print()
    input("  Elige un caballo y pulsa 'ENTER' ...")