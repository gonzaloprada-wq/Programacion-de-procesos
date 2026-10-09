from tenis import *


if __name__ == "__main__":

    ruta = "Proyectos/Tenis/data/datos.txt"

    import os
    print(os.getcwd())

    registros = leer_fichero(ruta)
    n = 3
    print("\n")
    print("\t", "PARTIDOS CON DESVIACIONES DE " + str(n) + " MINUTOS:")
    print("\t", "-----------------------------------------")
    print("\n")
    for p in desviaciones_media(registros, n):
        print("\t", "+", p)
        print("\n")

    print("\n")
    print("\t", "FECHAS CON MAYOR DIFERENCIA DE JUEGOS POR SUPERFICIE:")
    print("\t", "-----------------------------------------")
    for superficie, fechas in diccionario_diferencia_juegos_superficie(registros, n).items():
        print("\t", superficie, ":", fechas)