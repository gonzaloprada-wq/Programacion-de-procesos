import csv 
from collections import namedtuple

Partido = namedtuple('Partido','fecha,nombreRival,superficie,duracion,juegosGanados,juegosPerdidos,ganado')

def leer_fichero(nombre_fichero):

    partidos=[]

    with open(nombre_fichero, encoding='utf-8') as fichero:
        lector=csv.reader(fichero)
        next(lector)

        for linea in lector:

            fecha=linea[0]
            nombreRival=linea[1]
            superficie=linea[2]
            duracion=float(linea[3])
            juegosGanados=int(linea[4])
            juegosPerdidos=int(linea[5])
            ganado=linea[6] == "True"

            tupla=Partido(fecha, nombreRival, superficie, duracion, juegosGanados, juegosPerdidos, ganado)
            partidos.append(tupla)

    return partidos

def lee_fichero(registros):
    print('\tLeidos: ', len(registros), 'registros')
    print('\tMostrando')

    for registro in registros:
        print('\t', registro, sep=';')

def  desviaciones_media(partidos, n):

    media = sum(p.duracion for p in partidos)/len(partidos)

    listaTuplas = [(p.duracion- media, p) for p in partidos if p.duracion-media>=n]

    return listaTuplas

def diferencia_juego(partido):
    return partido.juegosGanados - partido.juegosPerdidos

def rival_mayor_porcentaje_victorias(partidos, superficie):

    diccionarioJugadas={}

    #Recorremos los partidos y guardamos en un dic las veces que se ha jugado con cierto 
    #en una superficie concreta
    for partido in partidos:

        if partido.superficie == superficie:

            clave = partido.nombreRival

            if clave in diccionarioJugadas:
                 
                 diccionarioJugadas[clave] += 1

            else:

                diccionarioJugadas[clave] = 1

    diccionarioGanadas={}

    for partido in partidos:

         if partido.superficie == superficie:

            clave= partido.nombreRival

            if clave in diccionarioGanadas and partido.ganado:

                diccionarioGanadas[clave] += 1

            elif partido.ganado:

                diccionarioGanadas[clave] = 1

            elif clave not in diccionarioGanadas and not partido.ganado:

                diccionarioGanadas[clave] = 0
           

    diccionarioResultados={}

    for clave in diccionarioJugadas:

        diccionarioResultados[clave]= 100.0*diccionarioGanadas[clave]/diccionarioJugadas[clave]
        
    return max(diccionarioResultados.items(), key=lambda t:t[1])


def diccionario_diferencia_juegos_superficie(partidos, n):

    superficies = {}

    for p in partidos:
        superficies.setdefault(p.superficie, []).append(p)

    resultado={}


    for superficie, lista in superficies.items():

        mejores=sorted(lista, key=diferencia_juego, reverse=True)[:n]

        resultado[superficie]=[p.fecha for p in mejores]

    return resultado
