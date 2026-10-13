from ventas import *




if __name__ == "__main__":

    ruta="Proyectos/Ventas/data/ventas.txt"

    registros=leer_fichero(ruta)

    print("\n")

    producto1="ProductoC"
    producto2="Producto2B"

    print("CLIENTES QUE COMPRARON", producto1, "Y", producto2)
    print("----------------------------------------------")
    print("\n")
    conjuntoResultado=clientes_producto1_y_producto2(registros, producto1, producto2)

    if len(conjuntoResultado)!=0:

        print(set(conjuntoResultado))
        print("\n")

    else:
        print("NO EXISTENTE CLIENTES QUE HAYAN COMPRADO DICHO PRODUCTO!!! ")
        print("\n")

    print("\n","PRODUCTOS Y SUS PORCENTAJES")
    print("---------------------------")
    print("\n")
    print(diccionario_porcentaje_cantidad_producto(registros))

    listaClientes={"ClienteB","ClienteC"}
    
   
    print("\n","PRODUCTO CON MAYORES VENTAS ENTRE CLIENTES")
    print("----------------------------------------------")
    print("\n")
    print(producto_mas_vendido(registros, listaClientes, 6))
    print("\n")
