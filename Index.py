import Cargar_archivo
import Graficar_ruta
import Graficar_mapa

def index():
    i=0
    while i != 2:
        print(" -------------------------------------")
        print("|                                     |")
        print("|  Pablo Daniel Fernández Chacón      |")
        print("|  Carné: 201807411                   |")
        print("|                                     |")
        print(" -------------------------------------")
        print("MENÚ: ")
        print("1. Cargar Archivo")
        print("2. Graficar Mapa")
        print("3. Graficar Ruta")
        print("4. Salir")
        elegir = input("Escoja un número y será su elección del menú: ")
        if str(elegir) == '1':
            Cargar_archivo.carga()
            print("¿Desea realizar alguna acción extra")
            i = 0
        elif str(elegir) == '2':
            Graficar_mapa.mapa()
            print("¿Desea realizar alguna acción extra")
            i = 0
        elif str(elegir) == '3':
            Graficar_ruta.rute()
            print("¿Desea realizar alguna acción extra")
            i = 0
        elif str(elegir) == '4':
            print("Adiós")
            i = 2;
        else:
            print("dato no valido")
index()
        
