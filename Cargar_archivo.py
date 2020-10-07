from tkinter import filedialog
import glob
from collections import defaultdict

def carga():
    while True:
        ruta = filedialog.askopenfilename()
        if ".txt" in ruta:
            fileNames = defaultdict(list)
            print("Archivo html cargado")
            fr = open(ruta, encoding="utf8")
            file_ = open("result.html","w")
            a = fr.readlines()
            b = len(a)
            k = []
            tablero = []
            ruta = []
            estacion = []
            errores = []
            temp = []
            html = ''
            simbolos = "¿¡?!@#$%^&*()_-+={}[]/.!"
            symbols = "¿¡?!@#$%^&*()_-+={}[]/.!"
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
                        k.append(h[j])
                elif len(h) != 1:
                    for j in range(0,len(h)):
                        k.append(h[j])
                        #print(i)
            q = len(h)
            for i in range(0,q):
                j = i+1;
                if k[i] == "ruta":
                    while k[j] != "/ruta":
                       ruta.append(k[j])
                       j+=1;
                elif k[j]== "estacIon":
                    while k[j] != "/estacion":
                        estacion.append(k[j])
                        j+=1
                elif k[j]== "estacion":
                    while k[j] != "/estacion":
                        estacion.append(k[j])
                        j+=1


            

            #tabla de Tokens sin errores
            #print("---------------------------------------------------------------------------------------------------------------------------")
            cont = 1;
            html += '<html><h1>RESULTADOS</h1><table border="1"><tr><th>No.</th><th>Lexema</th><th>Fila</th><th>Columna</th><th>Token</th></tr>'
            for i in range(0,b):
                temp = tablero[i]
                if len(tablero[i]) == 1 and str(tablero[i]) not in simbolos:
                    temp = tablero[i]
                    html += '<tr><td>'+ str(cont) +'</td><td>' + str(temp[0]) + '</td><td> '+ str(i+1) +'</td><td>1</td><td> '+ str(temp[0]) +'</td></tr>'
                    cont += 1
                elif len(tablero[i]) != 1 and str(tablero[i]) not in simbolos:
                    for j in range(0,len(tablero[i])):
                        temp = tablero[i]
                        #print(str(temp[j]))
                        html += '<tr><td>'+ str(cont) +'</td><td>' + str(temp[j]) + '</td><td> '+ str(i+1) +'</td><td>'+str(j+1)+'</td><td> '+ str(temp[j]) +'</td></tr>'
                        cont += 1
                        #print(str(i))
                temp = []
            html += '</table>'
            
            #tabla de Tokens con errores
            cont = 1;
            html += '<h1>Errores</h1><table border="1"><tr><th>No.</th><th>Fila</th><th>Columna</th><th>Token</th><th>Descripción</th></tr>'
            for n in range(0, b):
                for j in range(0,24):
                    if symbols[j] in tablero[n]:
                        #print("Hay: "+ symbols[j] + " posición: " + str(n))
                        #print(str(tablero[n]))
                        sim = symbols[j]
                        if len(tablero[n]) == 1:
                            #print("longitud 1")
                            html += '<tr><td>'+str(cont)+'</td><td>'+str(n+1)+'</td><td>1</td><td>'+str(symbols[j])+'</td><td>DESCONOCIDO</td></tr>'
                            cont +=1 
                        elif len(tablero) != 1:
                            #print("longitud " + str(len(tablero[n])))
                            temp = tablero[n]
                            for m in range(0,len(temp)):
                                #print(str(temp[m]))
                                if temp[m] == sim:
                                    #print("fila: "+ str(n+1) +" columna: "+ str(m+1))
                                    html += '<tr><td>'+ str(cont)+'</td><td>'+str(n+1)+'</td><td>'+str(m+1)+'</td><td>'+str(symbols[j])+'</td><th>DESCONOCIDO</td></tr>'
                                    cont +=1
                            temp = []
            html += '</table></html>'
            
            file_.write(html)    
            print(k)
            print("")
            print("rutas: " + str(ruta))
            print("")
            print("estaciones: " + str(estacion))
            print("")
            print("lugar de los errores: " + str(errores))
            print("")
            print("para tablero: " + str(tablero))
            file_.close();
            fr.close()
        return ruta
