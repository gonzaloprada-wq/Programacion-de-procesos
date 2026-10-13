from tenis import *


if __name__ == "__main__":

    ruta = "Proyectos/Tenis/data/datos.txt"

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
    print("\n")
    superficie="Tierra"
    print("\t", "CONTRINCANTE CON MAS TASAS DE DERROTAS EN "+str(superficie))
    print("\t", "-----------------------------------------------")
    print("\t",rival_mayor_porcentaje_victorias(registros, superficie))
    print("\n")