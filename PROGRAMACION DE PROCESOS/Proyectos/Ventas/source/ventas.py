import csv

from collections import namedtuple

Venta=namedtuple("Venta", "id,fecha,cliente,producto,cantidad,precio,beneficio")

def leer_fichero(ruta_fichero):

    tupla_resultado=[]

    with open(ruta_fichero, encoding="utf-8")as fichero:

        lector=csv.reader(fichero, delimiter=",", skipinitialspace="True")

        next(lector)

        for linea in lector:



            id=int(linea[0])
            fecha=linea[1]
            cliente=linea[2]
            producto=linea[3]
            cantidad=int(linea[4])
            precio=float(linea[5])
            beneficio=float(linea[6])

            tupla=Venta(id,fecha,cliente,producto,cantidad,precio,beneficio)
            tupla_resultado.append(tupla)

        return tupla_resultado
    
def clientes_producto1_y_producto2(ventas, producto1, producto2):

    clientes_compraron_producto1={actual.cliente for actual in ventas if actual.producto==producto1}
    clientes_compraron_producto2={actual.cliente for actual in ventas if actual.producto==producto2}

    return clientes_compraron_producto1 & clientes_compraron_producto2


def diccionario_porcentaje_cantidad_producto(ventas):

    diccionario={}

    cantidad_ventas_totales=sum(actual.cantidad for actual in ventas)

    diccionario=rellenar_diccionario(ventas)

    diccionar_final=diccionario_calcular_procentajes(diccionario, cantidad_ventas_totales)

    return diccionar_final



def rellenar_diccionario(ventas):

    diccionario={}

    for actual in ventas:

        if actual.producto in diccionario:

            diccionario[actual.producto]+=actual.cantidad
        else:

            diccionario[actual.producto]=actual.cantidad

    return diccionario


def diccionario_calcular_procentajes(diccionario, cantidad_ventas_totales):

    diccionario_final={}

    for indice in diccionario:

        diccionario_final[indice]=str(round((diccionario[indice]/cantidad_ventas_totales*100), 2))+" %"

    return diccionario_final


def producto_mas_vendido(ventas, clientes, numero_pedido):

    lista_filtrada=filtrado(ventas, clientes, numero_pedido)

    diccionario_productos=diccionario_productos_ventas(lista_filtrada)

    return max(diccionario_productos.items(), key=lambda t:t[1])

 
def filtrado(ventas, clientes, numero_pedido):

    lista_clientes_deseados=[venta for venta in ventas if venta.cliente in clientes]

    lista_clientes_ordenado=sorted(lista_clientes_deseados,reverse=True, key=lambda t:t.cantidad)[:numero_pedido]

    return lista_clientes_ordenado

def diccionario_productos_ventas(lista_filtrada):

    diccionario_productos={}

    for actual in lista_filtrada:

        if actual.producto in diccionario_productos:

            diccionario_productos[actual.producto]+=1
        else:

            diccionario_productos[actual.producto]=1

    return diccionario_productos