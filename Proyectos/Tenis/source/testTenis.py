from tenis import *
from pathlib import Path

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

    diferencia_goles=partido.juegos_ganados-partido.juegos_perdidos


    return diferencia_goles


def diccionario_diferencia_juegos_superficie(partidos, n):

    superficies = {}

    for p in partidos:
        superficies.setdefault(p.superficie, []).append(p)



    resultado={}


    for superficie, lista in superficies:

        mejores=sorted(lista, key=diferencia_juego, reverse=true)[:n]

        resultado[superficie]=[p.fecha for p in mejores]

    return resultado





if __name__ == "__main__":

    ruta = Path(__file__).parent.parent / "data" / "datos.txt"
    
    registros = leer_fichero(ruta)
    n=3
    print("\n")
    print("\t","PARTIDOS CON DESVIACIONES DE "+str(n)+ " MINUTOS:")
    print("\t","-----------------------------------------")
    print("\n")
    for p in desviaciones_media(registros, n):
        
        print("\t","+",p)
        print("\n")
       
    print(diccionario_diferencia_juegos_superficie(registros, n))
        

