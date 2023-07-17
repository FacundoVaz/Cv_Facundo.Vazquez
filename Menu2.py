#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACIAS import *
from menu import*
from principal import*

def lectura2(archivo, lista):
    nueva=archivo.readlines()
    palabra=""
    for i in range(len(nueva)):
        for letra in (nueva[i]):
            if (letra>="a" and letra<="z" or letra=="ñ") or (letra>="0" and letra <="9"):
                palabra=palabra+letra
            else:
                lista.append(palabra)
        palabra=""

def esta(jugador,nombres):
    False
    for elemento in nombres:
        if elemento==jugador:
            return True

def puntaje(nombres,mejores,jugador,puntos):
    auxMej=[]
    auxNom=[]

    i=0
    while i < (len(nombres)):
        if int(puntos)>= int(mejores[i]) and not(esta(jugador,auxNom)):
            auxMej.append(puntos)
            auxNom.append(jugador)
            auxMej.append(mejores[i])
            auxNom.append(nombres[i])
        else:
            auxMej.append(mejores[i])
            auxNom.append(nombres[i])
        i=i+1

    for i in range(len(auxMej)-1):
        nombres[i]=auxNom[i]
        mejores[i]=auxMej[i]


def menu2(puntos):
    res = (720,720)

    screen = pygame.display.set_mode(res)

    color = (255,255,255)

    color_light = (170,170,170)

    color_dark = (100,100,100)

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    #Abrir lista de nombres y puntos
    LiNombres=[]
    LiMejores=[]
    #Tomar las lista de los archivos
    nombres=open("nombres.txt","r")
    lectura2(nombres,LiNombres)
    nombres.close()
    mejores=open("mejores.txt","r")
    lectura2(mejores,LiMejores)
    mejores.close()

    #Nombre que no esté en la lista de nombres
    jugador=(input("Ingrese su nombre Máximo de 6 letras"))
    while esta(jugador,LiNombres) and len(jugador)<=6:
        jugador=input("Ingrese otro nombre")


    puntaje(LiNombres,LiMejores,jugador,puntos)

    titulo=defaultFont.render("Lograste " + str(puntos) + " puntos" , True , COLOR_LETRAS)
    top5=defaultFont.render("TOP 5" , True , COLOR_LETRAS)
    nombre0 = defaultFont.render(LiNombres[0] , True , COLOR_LETRAS)
    puntos0 =defaultFont.render(str(LiMejores[0]) , True , COLOR_LETRAS)
    nombre1 = defaultFont.render(LiNombres[1] , True , COLOR_LETRAS)
    puntos1 =defaultFont.render(str(LiMejores[1]) , True , COLOR_LETRAS)
    nombre2 = defaultFont.render(LiNombres[2] , True , COLOR_LETRAS)
    puntos2 =defaultFont.render(str(LiMejores[2]) , True , COLOR_LETRAS)
    nombre3 = defaultFont.render(LiNombres[3] , True , COLOR_LETRAS)
    puntos3 =defaultFont.render(str(LiMejores[3]) , True , COLOR_LETRAS)
    nombre4 = defaultFont.render(LiNombres[4] , True , COLOR_LETRAS)
    puntos4 =defaultFont.render(str(LiMejores[4]) , True , COLOR_LETRAS)
    puesto1=defaultFont.render("1." , True , COLOR_LETRAS)
    puesto2=defaultFont.render("2." , True , COLOR_LETRAS)
    puesto3=defaultFont.render("3." , True , COLOR_LETRAS)
    puesto4=defaultFont.render("4." , True , COLOR_LETRAS)
    puesto5=defaultFont.render("5." , True , COLOR_LETRAS)
    text=defaultFont.render("Reintentar" , True , COLOR_LETRAS)
    text2=defaultFont.render("Salir" , True , COLOR_LETRAS)

    #Reescribir los archivos de nombres y puntos
    nombres=open("nombres.txt","w")
    for elemento in LiNombres:
        nombres.write(elemento+"\n")
    nombres.close()
    mejores=open("mejores.txt","w")
    for elemento in LiMejores:
        mejores.write(str(elemento)+"\n")
    mejores.close()

    while True:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                if ev.type == pygame.QUIT:
                    pygame.quit()
                if ev.type==KEYDOWN:
                    if ev.key==K_ESCAPE:
                        pygame.quit()
                        quit()
            #Acción del click en botones
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= mouse[0] <= 240 and 500 <= mouse[1] <= 540:
                        main()
                if 560 <= mouse[0] <= 700 and 500 <= mouse[1] <= 540:
                        pygame.quit()


        screen.fill((0, 22, 142))



        mouse = pygame.mouse.get_pos()
        #Forma y color de botones cuando pasan por encima con el mouse.
        if 100 <= mouse[0] <= 240 and 500 <= mouse[1] <= 540:
            pygame.draw.rect(screen,color_light,[100,500,140,40])
        else:
            pygame.draw.rect(screen,color_dark,[100,500,140,40])

        if 560 <= mouse[0] <= 700 and 500 <= mouse[1] <= 540:
            pygame.draw.rect(screen,color_light,[560,500,140,40])
        else:
            pygame.draw.rect(screen,color_dark,[560,500,140,40])

        #Dibujar título
        screen.blit(titulo ,(260,100))
        screen.blit(top5 ,(315,200))
        #Dibujar puestos
        screen.blit(puesto1 ,(275,250))
        screen.blit(nombre0 ,(305,250))
        screen.blit(puntos0 ,(385,250))
        screen.blit(puesto2 ,(275,300))
        screen.blit(nombre1 ,(305,300))
        screen.blit(puntos1 ,(385,300))
        screen.blit(puesto3 ,(275,350))
        screen.blit(nombre2 ,(305,350))
        screen.blit(puntos2 ,(385,350))
        screen.blit(puesto4 ,(275,400))
        screen.blit(nombre3 ,(305,400))
        screen.blit(puntos3 ,(385,400))
        screen.blit(puesto5 ,(275,450))
        screen.blit(nombre4 ,(305,450))
        screen.blit(puntos4 ,(385,450))
        #Texto de botones
        screen.blit(text ,(120,510))
        screen.blit(text2 ,(580,510))




        pygame.display.update()