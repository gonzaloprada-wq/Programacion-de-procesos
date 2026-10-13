import csv
from collections import namedtuple
Atleta = namedtuple('Atleta', 'nombre,edad,pais,peso')

#pepe,20,italia,87.3
def leer_fichero(nombre_fichero):

    registros=[]

    #Esto abre el archivo
    with open(nombre_fichero, encoding='utf-8') as f:

        lector=csv.reader(f)

        next(lector) #esto sala la primera linea

        for linea in lector:

            nombre=linea[0]

            #Covierto a int
            edad = int(linea[1])

            pais = linea[2]

            peso = float(linea[3])

            tupla=Atleta(nombre,edad, pais,peso)

            registros.append(tupla)


    return registros

def edad_media(registros):

    res= 0.0
     
    for r in registros:

        res+=r.edad

    return res/len(registros)

#def num_atletas_por_pais(registros):
    

