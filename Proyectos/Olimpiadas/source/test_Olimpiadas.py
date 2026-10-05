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
    

    


if __name__ == "__main__":
    
    print("Proyecto olimpiadas")

    ruta = Path(__file__).parent.parent / "data" / "atletas.txt"

    registros = leer_fichero(ruta)

    test_lee_fichero(registros)

    print('\t',num_atletas_por_pais(registros))


    print('\t'"Atleta con mayor peso: ")

    atletaMayorPeso=atleta_mayor_peso(registros)[0]
    
    print('\t',atletaMayorPeso)