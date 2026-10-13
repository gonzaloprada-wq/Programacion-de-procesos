import csv

from collections import namedtuple

BatallaGOT = namedtuple('BatallaGOT', 'nombre rey_atacante rey_atacado gana_atacante muertes_principales comandantes_atacantes comandantes_atacados region num_atacantes num_atacados') 

def lee_batallas(fichero):

    listaFinal=[]

    with open(fichero, encoding="utf-8", ) as fichero_abierto:

        lector=csv.reader(fichero_abierto, delimiter=";")
        
        next(lector)

        for linea in lector:

            nombre=linea[0]
            rey_atacante=linea[1]
            rey_atacado=linea[2]
            gana_atacante= True if linea[3]=="win" else False
            muertes_principales=True if linea[4]==1 else False
            comandantes_atacantes=convertir_a_lista(tuple(linea[5].split(", ")))
            comandantes_atacados=convertir_a_lista(tuple(linea[6].split(", ")))
            region=linea[7]
            num_atacantes= None if linea[8].strip()=="" else int(linea[8].strip())
            num_atacados=None if linea[9].strip()=="" else int(linea[9].strip())

            tupla=BatallaGOT(nombre,rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados)
            listaFinal.append(tupla)
    return listaFinal


def convertir_a_lista(tupla):

    lista_comandantes=[]

    if len(tupla)>=1:

        for comandante in tupla:

            lista_comandantes.append(comandante.strip())
    
    return lista_comandantes



def imprime_batallas (batallas):

    print(len(batallas))
    print("\n")
    print("\n LISTADO DE LAS BATALLAS:")
    print("\n--------------------------------------------------------------------------------------------------------")
    for batalla_actual in batallas:

        print("\n\t---",batalla_actual)
        print("\n--------------------------------------------------------------------------------------------------------")

def suma_atacantes_rey(diccionario_reyes, batalla):

    if batalla.rey_atacante in diccionario_reyes:
                       
         diccionario_reyes[batalla.rey_atacante]+=batalla.num_atacantes    
    else:
        diccionario_reyes[batalla.rey_atacante]=batalla.num_atacantes

    return diccionario_reyes

def suma_atacados_rey(diccionario_reyes, batalla):

    if batalla.rey_atacado in diccionario_reyes:
                       
         diccionario_reyes[batalla.rey_atacado]+=batalla.num_atacados  
    else:
        diccionario_reyes[batalla.rey_atacado]=batalla.num_atacados

    return diccionario_reyes

def devolver_tupla_mayor_menor(diccionario_reyes):

    rey_mas_ejercito=max(diccionario_reyes, key=lambda k: diccionario_reyes[k])  

    rey_menos_ejercito=min(diccionario_reyes, key=lambda k: diccionario_reyes[k])  

    tupla_resultado=(rey_mas_ejercito, rey_menos_ejercito)

    return tupla_resultado

def reyes_mayor_menor_ejercito(batallas):

    diccionario_reyes={}

    for batalla in batallas:

        if batalla.num_atacantes is not None:

            diccionario_reyes=suma_atacantes_rey(diccionario_reyes, batalla)

        if batalla.num_atacados is not None:

            diccionario_reyes=suma_atacados_rey(diccionario_reyes, batalla)

    tupla_resultado=devolver_tupla_mayor_menor(diccionario_reyes)

    return tupla_resultado
    
    
def batallas_mas_comandantes(batallas, regiones, n):

    if regiones is not None:

        lista_tuplas=regiones_instanciadas(batallas, regiones)

    else:


def regiones_instanciadas(batallas, regiones):

    lista_tuplas=[]

    for batalla in batallas:

        if batalla.region in batallas:

            if batalla.nombre not in()