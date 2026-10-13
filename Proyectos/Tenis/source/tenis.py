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


def diccionario_diferencia_juegos_superficie(partidos, n):

    superficies = {}

    for p in partidos:
        superficies.setdefault(p.superficie, []).append(p)

    resultado={}


    for superficie, lista in superficies.items():

        mejores=sorted(lista, key=diferencia_juego, reverse=True)[:n]

        resultado[superficie]=[p.fecha for p in mejores]

    return resultado
