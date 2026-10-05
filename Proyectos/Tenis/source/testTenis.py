from tenis import *
from pathlib import Path

def lee_fichero(registros):
    print('\tLeidos: ', len(registros), 'registros')
    print('\tMostrando')

    for registro in registros:
        print('\t', registro, sep=';')

def  desviaciones_media(partidos, n)



if __name__ == "__main__":

    print("")

    ruta = Path(__file__).parent.parent / "data" / "datos.txt"

    registros = leer_fichero(ruta)

    desviaciones_media(registros, n)

