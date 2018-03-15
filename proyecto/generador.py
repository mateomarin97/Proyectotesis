#!/usr/bin/env python3
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
import time
#Vamos ahcer una funcion que cambie los planos,stack es una lista donde cada elemento es una imagen
def planos1(stack):
    nplanos=len(stack)
    #numero de filas en los planos originales
    nfilas=np.asarray(stack[0]).shape[0]
    #numero de columnas en los planos originales
    ncolumnas=np.asarray(stack[0]).shape[1]
    stacknuevo=[]
    #Volvemos el stack de imagenes un array
    astack=[]
    for i in range(nplanos):
        astack.append(np.asarray(stack[i]))
    for j in range(ncolumnas):
        planonuevo=[]
        for k in range(nplanos):
            listaauxiliar=[]
            for i in range(nfilas):
                listaauxiliar.append(astack[k][i][j])
                print("Lista auxiliar 1 creado "+str(i)+"/"+str(nfilas))
            planonuevo.append(listaauxiliar)
        planonuevo=np.asarray(planonuevo)
        stacknuevo.append(Image.fromarray(planonuevo))
        print("Plano nuevo 1 creado "+str(j)+"/"+str(ncolumnas))
    return stacknuevo
        
    

    
#Vamos ahcer una funcion que cambie los planos,stack es una lista donde cada elemento es una imagen
def planos2(stack):
    nplanos=len(stack)
    #numero de filas en los planos originales
    nfilas=np.asarray(stack[0]).shape[0]
    #numero de columnas en los planos originales
    ncolumnas=np.asarray(stack[0]).shape[1]
    stacknuevo=[]
    #Volvemos el stack de imagenes un array
    astack=[]
    for i in range(nplanos):
        astack.append(np.asarray(stack[i]))
    for i in range(nfilas):
        planonuevo=[]
        for k in range(nplanos):
            listaauxiliar=[]
            for j in range(ncolumnas):
                listaauxiliar.append(astack[k][i][j])
                print("Lista auxiliar 2 creado "+str(j)+"/"+str(ncolumnas))
            planonuevo.append(listaauxiliar)
        planonuevo=np.asarray(planonuevo)
        stacknuevo.append(Image.fromarray(planonuevo))
        print("Plano nuevo 2 creado "+str(i)+"/"+str(nfilas))
    return stacknuevo




#Vamos ahcer una funcion que deshaga el efecto de planos1,stack es una lista donde cada elemento es una imagen
def planos1inv(stack):
    nplanos=len(stack)
    #numero de filas en los planos originales
    nfilas=np.asarray(stack[0]).shape[0]
    #numero de columnas en los planos originales
    ncolumnas=np.asarray(stack[0]).shape[1]
    stacknuevo=[]
    #Volvemos el stack de imagenes un array
    astack=[]
    for i in range(nplanos):
        astack.append(np.asarray(stack[i]))
    for i in range(nfilas):
        planonuevo=[]
        for j in range(ncolumnas):
            listaauxiliar=[]
            for k in range(nplanos):
                listaauxiliar.append(astack[k][i][j])
                print("Lista auxiliar 1 inv creado "+str(k)+"/"+str(nplanos))
            planonuevo.append(listaauxiliar)
        planonuevo=np.asarray(planonuevo)
        stacknuevo.append(Image.fromarray(planonuevo))
        print("Plano nuevo 1 inv creado "+str(i)+"/"+str(nfilas))
    return stacknuevo


#Vamos hacer una funcion que deshaga el efecto de planos1,stack es una lista donde cada elemento es una imagen
def planos2inv(stack):
    nplanos=len(stack)
    #numero de filas en los planos originales
    nfilas=np.asarray(stack[0]).shape[0]
    #numero de columnas en los planos originales
    ncolumnas=np.asarray(stack[0]).shape[1]
    stacknuevo=[]
    #Volvemos el stack de imagenes un array
    astack=[]
    for i in range(nplanos):
        astack.append(np.asarray(stack[i]))
    for i in range(nfilas):
        planonuevo=[]
        for k in range(nplanos):
            listaauxiliar=[]
            for j in range(ncolumnas):
                listaauxiliar.append(astack[k][i][j])
                print("Lista auxiliar 2 inv creado "+str(j)+"/"+str(ncolumnas))
            planonuevo.append(listaauxiliar)
        planonuevo=np.asarray(planonuevo)
        stacknuevo.append(Image.fromarray(planonuevo))
        print("Plano nuevo 2 inv creado "+str(i)+"/"+str(nfilas))
    return stacknuevo


#stack es el stack, a1,a2,a3 los angulos a rotar respecto a cada eje, contador un numero que me ayuda a saber en que carpeta guardar
#el stack
def rotaciontotal(stack,a1,a2,a3,contador):
    #Creamos la carpeta
    os.system('mkdir ./'+str(contador))
    #rotamos a1 grados respecto al primer eje
    for i in range(len(stack)):
        stack[i]=stack[i].rotate(a1)
        print("Primera rotacion "+str(i)+"/"+str(len(stack)))
    #Cambiamos la orientacion del stack
    stack=planos1(stack)
    #rotamos a2 grados respecto al segundo eje
    for i in range(len(stack)):
        stack[i]=stack[i].rotate(a2)
        print("Segunda rotacion "+str(i)+"/"+str(len(stack)))
    #Regresamos a la orientacion original
    stack=planos1inv(stack)
    #Pasamos a la segunda orientacion
    stack=planos2(stack)
    #rotamos a3 grados respecto al tercer eje
    for i in range(len(stack)):
        stack[i]=stack[i].rotate(a3)
        print("Tercera rotacion "+str(i)+"/"+str(len(stack)))
    #Volvemos a la orientacion original
    stack=planos2inv(stack)
    #Ahora guardamos cada una de las imagenes se stack
    for i in range(len(stack)):
        np.savetxt("./"+str(contador)+"/"+str(i)+".tif",stack[i])
    contador=contador+1
    return contador


#Cargamos el stack 1
os.system('ls ./1 > nombres1.dat')
#Ahora cargamos dicha lista
with open('nombres1.dat', 'r') as myfile:
    data=myfile.readlines()
#Estons nombres tienen un /n que me molesta asi que lo voy a quitar, ademas el ultimo elemento no es una imagen
nombres=[s.replace('\n','') for s in data]
#cargamos las imagenes
img1=[]
for i in nombres:
    img1.append(Image.open("./1/"+str(i)))

#Generamos el stack 10
tiempoi=time.time()
hola=rotaciontotal(img1,15,15,15,10)
tiempofin=time.time()
np.savetxt("tiempo.dat",np.array([tiempofin-tiempoi]))
