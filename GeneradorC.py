import os     # para limpiar 
from time import sleep    # para dormir ciertas partes 
import random    # importante (generar las contraseñas)

# lo siguiente son colores que ultilizaré
ROJO = '\033[0;31m'
GRIS = '\033[1;30m'
VERDE = '\033[1;32m'
AZUL = '\033[0;34m'
AMARILLO = '\033[1;33m'
LILA = '\033[0;35m'
CIAN = '\033[0;36m'
BLANCO = '\033[1;37m'
# variables de el largo de contraseñas  ( rango )
INICIO = 33
FIN = 126
# casilla
CASILLA = LILA + '[' + GRIS + '+' + LILA + ']'
# domir algunas cosas por un determinado tiempo
TIEMPO = 0.7
# el archivo donde se guardará las contraseñas
ARCHIVO = "Libreta-A.txt"
# Titulo
TITULO  = AMARILLO + "Generador de contraseñas"
# presentacion #1
PRESENTACION1 = ROJO + "Nota: Para abrir el archivo donde se almacenó tu"
PRESENTACION2  = ROJO + "contraseña tienes que que poner lo siguiente"
PRESENTACION3 = ROJO + '"cat Libreta-A.txt", y listo!!'  
# proceso de la contraseña
def proceso():
    while True:
        os.system("clear")
        print (TITULO.center(82, "-") + "---")
        print (PRESENTACION1.center(82, " "))
        print (PRESENTACION2.center(82, " "))
        print (PRESENTACION3.center(82, " "))
        print ("\n")
        longitud = input(CASILLA + VERDE + " Ingrese un número: " + CIAN)
        try:
            longitud = int(longitud)
            if longitud > int(0) and longitud <= int(20):
                break
            else:
                print (ROJO + "ingresa valor númerico aceptable")
                sleep(0.9)
        except ValueError:
            print (ROJO + "Ingrese valor númerico")
            sleep(TIEMPO)
            os.system("clear")
    for x in range(longitud):
        aleatorio_numero = random.randint(INICIO, FIN)
        aleatorio_caracter = chr(aleatorio_numero)
        print (aleatorio_caracter, end="")
        print (LILA + ''' | ''')
        print (AZUL + "   >>>> " + GRIS + ARCHIVO)
        with open(ARCHIVO, "a") as archivo:
            archivo.write(aleatorio_caracter)
        
proceso()

print (" ")
regresar = input(CASILLA + VERDE  + " ¿Quieres regresar?[y/n] " + CIAN).lower()
while regresar != "y" and regresar != "n":
    print (ROJO + "Opcion invalida")
    sleep(TIEMPO)    
    os.system("clear")
    print (TITULO.center(82, "-") + "---")
    print (PRESENTACION1.center(82, " "))
    print (PRESENTACION2.center(82, " "))
    print (PRESENTACION3.center(82, " "))
    print ("\n")
    regresar = input(CASILLA + VERDE  + " ¿Quieres regresar?[y/n]" + CIAN).lower()
    
        
    