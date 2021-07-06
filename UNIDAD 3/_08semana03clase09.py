def cicloForParaDict():
    datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
    }
    claves = list( datos_basicos.keys())
    valores = list(datos_basicos.values())
    clavesYValores = list(datos_basicos.items())
    
    print ("claves: ", claves)
    print ("valores: ", valores)
    print ("claves y valores: ", clavesYValores)
    
    
    #primer ciclo, acceder directamente a las claves del diccionario
    print ("Primer ciclo: Acceder a las claves y valores del diccionario: ")
    for clave in datos_basicos:
        print("Key: ", clave, " Value: ", datos_basicos[clave])
    
    #segundo ciclo, acceder directamente a las claves mediante keys
    print ("\nSegundo ciclo: Acceder directamente a las claves por Keys")
    for clave in datos_basicos.keys():
        print("Key: ", clave, " Value: ", datos_basicos[clave])
        
    #Tercer ciclo, acceder solo a los valores del diccionario mediante values
    print ("\nTercer ciclo: Acceder solo a los valores del diccionario")
    for valor in datos_basicos.values():
        print ("Value: ", valor)
    
    #Cuarto ciclo, acceder tanto a la clave como al valor mediante items
    print ("\nCuarto ciclo: Acceder a la clave y al valor mediante items")
    for clave, valor in datos_basicos.items():
        print("Key: ", clave, " Value: ", valor)

#cicloForParaDict()

def listas1():
    lista = [ ]
    print (lista)
    lista2 = list()
    print (lista2)
    lista3 = [0 for x in range(5)]
    print (lista3)
#listas1()

def listas2():
    lista = [1,2,3,5,8,9,1,2,1,6]
    print (lista)
    lista[3] = {'GATO':lista[3]}
    #lista[3]= 'GATO'
    print (lista)
#listas2()

def listas3():
    versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 0, -80]
    print (versiones_plone)
    versiones_plone.sort(reverse=True)
    print(versiones_plone)
#listas3()

def listas4():
    vocales = 'aeiou'
    for letra in 'operadores':
        if letra in vocales:
                print(letra)
#listas4()


def listas5():
    listaPreguntas = ['nombre', 'objetivo', 'sistema operativo']
    listaRespuestas = ['Ana', 'aprender Python y Plone', 'Linux']
    
    n = len(listaPreguntas)
    for i in range (n):
        print ("¿Cual es tu ", listaPreguntas[i], ". La respuesta es: ", listaRespuestas[i])
    
    
    listaPreguntas = ['nombre', 'objetivo', 'sistema operativo', 'fecha de nacimiento']
    listaRespuestas = ['Ana', 'aprender Python y Plone', 'Linux']
    #aqui la fecha de nacimiento no será tenida en cuenta, debido a que en la listaRespuestas no hay un elemento
    #relacionado con  la fecha de nacimiento
    for x, y in zip(listaPreguntas, listaRespuestas):
        print('¿Cual es tu {0}?, la respuesta es: {1}.'.format(x, y))
       
listas5()
        
    