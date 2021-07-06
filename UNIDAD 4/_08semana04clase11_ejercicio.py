'''
Desarrollar una función que reciba como parámetro un diccionario de resultados
de partidos de futbol y devuelva el nombre de los paises participantes en una lista
'''
def listaPaises (diccionario:dict) -> list:
    
    #lista = list()
    conjunto = set()
    for clave, valor in diccionario.items():
        #print (clave[0], '[',valor[0], '] - [', valor[1],']',clave[1])
        #lista.append(clave[0])
        #lista.append(clave[1])
        conjunto.add (clave[0])
        conjunto.add (clave[1])
    
    #lista = list( set(lista) )
    lista = list(conjunto)
        
    return lista

resultados = {
        ('Honduras', 'Chile'): (1, 1),
        ('Espana', 'Suiza'): (0, 1),
        ('Suiza', 'Chile'): (0, 0),
        ('Espana', 'Honduras'): (2, 0),
        ('Suiza', 'Honduras'): (1, 0),
        ('Espana', 'Chile'): (2, 1),
}

print (listaPaises(resultados))



