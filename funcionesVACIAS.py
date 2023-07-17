from principal import *
from configuracion import *
from funcionesSeparador import *


import random
import math



def lectura(archivo, lista):
    nueva=archivo.readlines()
    palabra=""
    for i in range(len(nueva)):
        for letra in (nueva[i]):
            if letra>="a" and letra<="z" or letra=="ñ":
                palabra=palabra+letra
            else:
                lista.append(palabra)
        palabra=""

def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    nueva=random.choice(listaDeSilabas)
    x=random.randrange(ANCHO-70)
    y=0
    #Reconocer si la x generada ya está en la lista de posiciones.
    esta=False
    for i in range(len(posiciones)):
        if (posiciones[i][0])==x:
            esta=True
    #Agregar la sílaba sólo si x es divisible por 2 y no está en la lista de posiciones.
    if x%3==0 and  not (esta):
        posiciones.append((x,y))
        silabasEnPantalla.append(nueva)
    for i in range(len(posiciones)):
        y=int(posiciones[i][1])
        if y<468:
            x=int(posiciones[i][0])
            y=y+10
            posiciones[i]=(x,y)
    #Borramos las silabas y agregamos una nueva en la parte superior de la pantalla.
        else:
            silabasEnPantalla.pop(i)
            posiciones.pop(i)
            silabasEnPantalla.append(nueva)
            posiciones.append((x,0))
        y=0


def nuevaSilaba(silabas):
    nueva=random.choice(silabas)
    return nueva

def quitar(candidata,silabasEnPantalla,posiciones):
    silabas=dameSilabas(candidata)
    auxSil=[]
    auxPos=[]
    #Reconocer si las silabas de candidata están en pantalla.
    for i in range (len(silabasEnPantalla)):
        if (silabasEnPantalla[i]) in silabas and (silabasEnPantalla[i]) not in auxSil:
            auxSil.append(silabasEnPantalla[i])
            auxPos.append(posiciones[i])
    #Eliminar las silabas y sus posiciones.
    for elemento in auxSil:
        silabasEnPantalla.pop(silabasEnPantalla.index(elemento))
    for elemento in auxPos:
        posiciones.pop(posiciones.index(elemento))


def dameSilabas(candidata):
    lista=[]
    nueva1=""
    nueva=separador(candidata)+"-"
    for letra in nueva:
        #Agrega las letras a la nueva cadena
        if letra>="a" and letra<="z" or letra=="ñ":
            nueva1=nueva1+letra
        #Cuando se encuentra con el "-", agrega la cadena a la lista.
        else:
            lista.append(nueva1)
            nueva1=""
    return lista


def esValida(candidata,silabasEnPantalla,lemario):
    silabas=dameSilabas(candidata)
    cont=0
    contr=len(silabas)
    for elemento in silabas:
        if elemento in silabasEnPantalla:
            cont=cont+1
    if candidata in lemario and cont==contr:
        return True
    else:
        return False

def puntos(candidata):
    puntos=0
    vocales=("aeiou")
    consDificil=("jkqwxyz")
    for letra in candidata:
        if letra in vocales:
            puntos=puntos+1
        if letra not in vocales and letra not in consDificil:
            puntos=puntos+2
        if letra in consDificil:
            puntos=puntos+5
    return puntos

def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    if esValida(candidata,silabasEnPantalla,lemario):
        quitar(candidata,silabasEnPantalla,posiciones)
        sonido.play()
        return (puntos(candidata))
    else:
        return(0)


