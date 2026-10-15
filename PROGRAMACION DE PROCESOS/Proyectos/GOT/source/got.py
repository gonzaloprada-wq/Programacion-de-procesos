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

    lista_batallas_comandantes=[]
 
    if regiones is not None:

        lista_batallas_comandantes=lista_tuplas(batallas, regiones)

    else:

        regiones=todas_las_regiones(batallas)
        
        lista_batallas_comandantes=lista_tuplas(batallas, regiones)

    if n is None or n == 0:

       return lista_batallas_comandantes

    else:

        lista_batallas_comandantes=sorted(lista_batallas_comandantes, key=lambda t:t[1], reverse=True)[:n]

        return lista_batallas_comandantes

        
def lista_tuplas(batallas, regiones):

    lista_nombre_batallas=[]


    for batalla in batallas:

        if batalla.region in regiones:

            if batalla.nombre not in lista_nombre_batallas:

                lista_nombre_batallas.append((batalla.nombre , (len(batalla.comandantes_atacantes)+len(batalla.comandantes_atacados))))

    
    return lista_nombre_batallas


def todas_las_regiones(batallas):

    lista_regiones=[batalla.region for batalla in batallas]

    return lista_regiones

def rey_mas_victorias(batallas, rol_batalla):

    diccionario_batallas=diccionario_reyes_vacio(batallas)

    diccionario_final=rellenar_batallas(batallas, rol_batalla, diccionario_batallas)

    rey_ganador=determinar_rey_mayor(diccionario_final)

    return rey_ganador

def diccionario_reyes_vacio(batallas):

    diccionario_batallas={}

    for batalla in batallas:

        if batalla.rey_atacante not in diccionario_batallas:

            diccionario_batallas[batalla.rey_atacante]=0

        if batalla.rey_atacado not in diccionario_batallas:
            
            diccionario_batallas[batalla.rey_atacado]=0

    return diccionario_batallas

def rellenar_batallas(batallas, rol, diccionario_batallas):

    for batalla in batallas:

        if (rol=="atacante" and batalla.gana_atacante) or rol is None:

            diccionario_batallas[batalla.rey_atacante]+=1
        
        if (rol=="atacado" and not batalla.gana_atacante) or rol is None:

             diccionario_batallas[batalla.rey_atacado]+=1

    return diccionario_batallas

def determinar_rey_mayor(lista_reyes_victorias):

    rey_ganador = max(lista_reyes_victorias.items(), key=lambda t: t[1])[0]

    return rey_ganador


    