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