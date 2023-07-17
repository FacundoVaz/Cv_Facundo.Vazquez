from funcionesVACIAS import*

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



LiNombres=[]
LiMejores=[]

nombres=open("nombres.txt","r")
lectura2(nombres,LiNombres)
nombres.close()
mejores=open("mejores.txt","r")
lectura2(mejores,LiMejores)
mejores.close()
jugador=(input("Ingrese su nombre"))
puntos=110

print(LiMejores)
print(LiNombres)

def esta(jugador,nombres):
    False
    for elemento in nombres:
        if elemento==jugador:
            return True

def puntaje(nombres,mejores,jugador,puntos):
    auxMej=[]
    auxNom=[]

    i=0
    while i < (len(nombres)-1):
        if puntos>= int(mejores[i]) and not(esta(jugador,auxNom)):
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

puntaje(LiNombres,LiMejores,jugador,puntos)
print(LiNombres,LiMejores)

nombres=open("nombres.txt","w")
for elemento in LiNombres:
    nombres.write(elemento+"\n")
nombres.close()
mejores=open("mejores.txt","w")
for elemento in LiMejores:
    mejores.write(str(elemento)+"\n")
mejores.close()