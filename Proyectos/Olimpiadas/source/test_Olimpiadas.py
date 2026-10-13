from olimpiadas import *
from pathlib import Path

print()
print("Test de la funcion lee_fichero")

def test_lee_fichero(registros):
    print()
    print('\tLeidos: ', len(registros), 'registros')
    print('\tMostrando los tres primeros')

    for r in registros[:3]:
        print('\t', r, sep='')

    
def num_atletas_por_pais(registros):
    diccionario={}
    print()
    print('\tMostrando lista de paises/personas: ')

    for atleta in registros:
        clave = atleta.pais
        if clave in diccionario:
             diccionario[clave] += 1  
        else:
            diccionario[clave] = 1

    return diccionario 

def atleta_mayor_peso(registros):

    return sorted(registros, key=lambda t:t[3], reverse="true")
    
def pais_mayor_peso_medio(registros):

    pesos = {}

    for registro in registros:

        pesos.setdefault(registro[2], []).append(float(registro[3]))

    mejor_pais = ""
    mayor_media = 0

    for pais in pesos:

        media = sum(pesos[pais]) / len(pesos[pais])

        if media > mayor_media:

            mayor_media = media
            mejor_pais = pais

    return mejor_pais
    

def metodozip(registros:list)->int:
        lis=[]
        registros=sorted(registros, key=lambda t:t.edad)

        for a,b in zip(registros,registros[:1]):
        
             lis.append(b.edad-a.edad)
        
        return max(lis)


if __name__ == "__main__":
    
    print("Proyecto olimpiadas")

    ruta = Path(__file__).parent.parent / "data" / "atletas.txt"

    registros = leer_fichero(ruta)

    test_lee_fichero(registros)

    print('\t',num_atletas_por_pais(registros))


    print('\n','\t'"Atleta con mayor peso: ")

    atletaMayorPeso=atleta_mayor_peso(registros)[0]
    
    print('\t',atletaMayorPeso)