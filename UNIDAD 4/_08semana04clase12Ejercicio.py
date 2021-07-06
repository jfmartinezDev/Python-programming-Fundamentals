def addDestino(itinerarios:list):
    #añadiendo un nuevo itinerario
    nombre = str(input('¿Cual es el nombre del destino que desea añadir? '))
    noches = int(input('¿Cuantas noches desea para este destino? '))
    lista = [nombre, noches]
    itinerarios.append(lista)
    print ('Asi va su itinerario ', itinerarios)

def deleteItinerario (itinerarios:list):
    #Eliminar un itinerario
    nombre = str(input('¿Cual es el nombre del destino que desea eliminar? '))
    posicionDestino = 0
    bandera = False
    for i in range (len(itinerarios)):
        if (nombre == itinerarios[i][0]):
            posicionDestino = i
            bandera = True
    if (bandera == False):
        print ('Ese destino no existe en la lista de itinerarios')

    itinerarios.pop(posicionDestino)
    print ('Asi va su itinerario ', itinerarios)

def addNight (itinerarios:list):
    #Añadir una noche a un destino en el itinerario
    nombre = str(input('¿Cual es el nombre del destino en el cual desea añadir mas noches? '))
    bandera = False
    for i in range (len(itinerarios)):
        if (nombre == itinerarios[i][0]):
            bandera = True
            cantidadNoches  = int(input('Cuantas noches desea usted añadir? '))
            itinerarios[i][1] += cantidadNoches
    if (bandera == False):
        print ('Ese destino no existe en la lista de itinerarios')
    print ('Asi va su itinerario ', itinerarios)

def funcionPrincipal(itinerarios:list):
    continuar = 'si'
    while (continuar == 'si'):
        print ('Bienvenido...')
        print ('Seleccione la opcion que usted desea realizar: ')
        print ('1. Añadir un nuevo destino')
        print ('2. Eliminar un destino de su itinerario')
        print ('3. Añadir una noche a un destino')
        opcion = int(input('Opcion: '))
        
        if (opcion == 1):
            addDestino(itinerarios)
        elif(opcion == 2):
            deleteItinerario(itinerarios)
        elif (opcion == 3):
            addNight (itinerarios)
        else:
            print ('Chau')
    
        continuar = str(input('Desea repetir todo el proceso nuevamente? '))
        if (continuar == 'si'):
            continue
        else:
            break
    
    
#lista itinerarios donde la posicion 0 será el nombre del destino y la posicion 1 seran las noches

itinerarios = [['Santa Marta',1],
               ['Cartagena',2],
               ['San Andres',4]]
print ('Itinerario Original ', itinerarios)

for i in range(len(itinerarios)):
	print(f"Destino: {itinerarios[i][0]}, Noches: {itinerarios[i][1]}")
	
funcionPrincipal (itinerarios)



'''itinerarios[0], itinerarios[-1] = itinerarios[-1], itinerarios[0]
print ('Asi va su itinerario ', itinerarios)'''