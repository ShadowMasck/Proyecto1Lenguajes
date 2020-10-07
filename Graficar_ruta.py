from tkinter import filedialog
from graphviz import Digraph
import os
import random

def rute():
    while True:
        ruta = filedialog.askopenfilename()
        if ".txt" in ruta:
            print("Archivo recibido")
            fr = open(ruta, encoding="utf8")
            a = fr.readlines()
            b = len(a)
            #print(b)
            k = []
            tablero = []
            ruta = []
            estacion = []
            datosruta = []
            datosestacion = []
            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            temp5 = []
            corto = []
            first = ("Super", "Retarded", "Great", "Sexy", "Vegan", "Brave", "Shy", "Cool", "Poor", "Rich", "Fast", "Gummy", "Yummy", "Masked", "Unusual", "American", "Bisexual", "MLG", "Mlg", "lil", "Lil")
            second = ("Coder", "Vegan", "Man", "Hacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Killer", "Woman", "Programmer", "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper", "Quickscoper")
            firrst = random.choice(first)
            seccond = random.choice(second)
            name = (firrst + "_" + seccond + ".gv")
            simbolos = "¿¡?!@#$%^&*()_-+={}[]"
            symbols = "!@#$%^&*()_-+={}[]"
            for i in range(0,b):
                c = a[i]
                d = c.replace('<',' ')
                e = d.replace('>',' ')
                f = e.replace('\r',' ')
                g = f.replace('\n',' ')
                h = g.split()
                tablero.append(h)
                if len(h) == 1:
                    for j in range(0,len(h)):
                        if str(h[j]) not in simbolos:
                            k.append(h[j])
                else:
                    for j in range(0,len(h)):
                        if str(h[j]) not in simbolos:
                            k.append(h[j])
            q = len(k)
            for i in range(0,q):
                j = i +1 
                if k[i] == "ruta":
                    #print("Hay rutas en: " + str(i))
                    if j != q:
                        while k[j] != "/ruta":
                            ruta.append(k[j])
                            j += 1
                            #print("dentro del rango: "+str(j))
                elif k[i] == "estacion" or k[i] == "estacIon":
                    #print("Hay estaciones en: " +str(i))
                    if j != q:
                        while k[j] != "/estacion":
                            estacion.append(k[j])
                            j += 1
            #Separamos las rutas
            r = len(ruta)
            for i in range(0,r):
                if ruta[i].upper() == "NOMBRE" and ruta[i+1].upper()!= "INICIO"and ruta[i+1].upper()!= "FIN" and ruta[i+1].upper()!= "PESO":
                    datosruta.append(ruta[i+1].upper())
                    datosruta.append("")
                    datosruta.append("")
                    datosruta.append("")
                elif ruta[i].upper() == "PESO" and ruta[i+1].upper() != "NOMBRE" and ruta[i+1].upper()!= "INICIO"and ruta[i+1].upper()!= "FIN":
                    temp1.append(ruta[i+1])
                elif ruta[i].upper() == "INICIO" and ruta[i+1].upper() != "PESO" and ruta[i+1].upper() != "NOMBRE" and ruta[i+1].upper()!= "FIN":
                    temp2.append(ruta[i+1].upper())
                elif ruta[i].upper() == "FIN" and ruta[i+1].upper() != "INICIO" and ruta[i+1].upper() != "PESO" and ruta[i+1].upper() != "NOMBRE":
                    temp3.append(ruta[i+1].upper())
            print(ruta)
            print(datosruta)
            print(temp1)
            print(temp2)
            print(temp3)

            #colocamos datos en rutas      
            dr = len(datosruta)
            j = 0
            for i in range(1,dr,4):
                datosruta[i] = temp1[j]
                j += 1
            j = 0
            for i in range(2,dr,4):
                datosruta[i] = temp2[j]
                j += 1
            j = 0
            for i in range(3,dr,4):
                datosruta[i] = temp3[j]
                j += 1
            
            
            #print("")
            #print("pesos: " + str(temp1) + "inicios: " + str(temp2) + "final: " + str(temp3))
            #print("")
            print("Todas las rutas: "+str(datosruta))

            #separamos las estaciones

            #print("")
            #print("estacion: " +str(estacion))
            e = len(estacion)

            
            for i in range(0,e):
                if estacion[i] == "nombre":
                    datosestacion.append(estacion[i+1].upper())
                    datosestacion.append("")
                    datosestacion.append("")
                elif estacion[i] == "estado":
                    temp4.append(estacion[i+1].upper())
                elif estacion[i] == "color":
                    temp5.append(estacion[i+1].upper())

            #colocamos datos en estacion         
            de = len(datosestacion)
            j = 0
            for i in range(1,de,3):
                datosestacion[i] = temp4[j]
                j += 1
            j = 0
            for i in range(2,de,3):
                datosestacion[i] = temp5[j]
                j += 1
            
            
            #print("")
            #print("estados: " + str(temp4) + "color: " + str(temp5))
            #print("")
            print("Todas las estaciones: "+str(datosestacion))
            #print("")
            ldr = len(datosruta)
            orden = sorted(temp1)
            for i in range(0,3):
                for z in range(1,ldr,4):
                    if orden[i] == datosruta[z]:
                        corto.append(datosruta[z-1])
                        corto.append(datosruta[z])
                        corto.append(datosruta[z+1])
                        corto.append(datosruta[z+2])
            print("Ruta Corta: "+str(corto))
            #print(k)
            #print("")
            #print("cantidad de datos: " + str(q))
            #print("")
            #print("rutas: " + str(ruta))
            #print("")
            #print("estaciones: " + str(estacion))

            #Se Grafica
            f = Digraph('finite_state_machine', filename=name)
            f.attr(rankdir='LR', size='8,5')

            #tomamos datos de los arreglos
            f.attr('node', shape='circle')
            le = len(datosestacion)
            for i in range(0,le,3):
                if datosestacion[i] in corto:
                    f.node(''+str(datosestacion[i])+" estado: " +datosestacion[i+1], fillcolor=''+datosestacion[i+2], color=''+datosestacion[i+2])

            

            f.attr('node', shape='circle')
            lr = len(datosruta)
            for i in range(0,lr,4):
                if datosruta[i+1] in corto:
                    #print("está")
                    f.edge(datosruta[i+2], datosruta[i+3], label=''+datosruta[i]+' peso: '+datosruta[i+1], color="red", )
                    

            f.view()
            print("Gráfica creada")
            fr.close()
        return ruta
