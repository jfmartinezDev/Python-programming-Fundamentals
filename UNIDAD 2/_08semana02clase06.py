#miercoles

def operacionesCadenas():
    palabra = 'banana'
    palabra_nueva = palabra.upper()
    print(palabra_nueva)

    palabra = 'limon'
    indice = palabra.find('n')
    print(indice)
    
    palabra = 'azucar'
    print (palabra.find('uc'))
    
    frase = 'Bienvenidos a la UTP y a MisionTIC22'
    print (frase.find('a', 3)) #posicion 12
    print (frase.find('a', 13)) #posicion 15
    print (frase.find('a', 16)) #posicion 23    
    
    
    print ("palabra1palabra2")
    print ("palabra1\tpalabra2")
    print ("palabra1\npalabra2")
    print (r"palabra1\tpalabra2")
    
    camellos = 0
    vacas = 200
    print ('He visto %d camellos y %d vacas' % ( camellos, vacas))
    cadena = "un uno, un dos, un tres"

    print (cadena.count("un"))        # Saca 4, hay 4 "un" en cadena.
    print (cadena.count("un",10))     # Saca 1, hay 1 "un" a partir de la posición 10 de cadena.
    print (cadena.count("un",0,10))   # Saca 3, hay 3 "un" entre la posición 0 y la 10.       
    
    cadena = "un uno, un dos, un tres"

    print (cadena.replace("un", "XXX"))        # saca por pantalla "XXX XXXo, XXX dos, XXX tres"
    print (cadena.replace("un", "XXX", 2))     # Sólo reemplaza 2 "un", así que saca por pantalla "XXX XXXo, un dos, un tres"   
    # saca "El valor es 12
    print ("El valor es {}".format(12))

    # saca "El valor es 12.3456
    print ("El valor es {}".format(12.3456))

    # Tres conjuntos {}, el primero para el primer parámetro de format(), el segundo para el segundo
    # y así sucesivamente.
    # saca "Los valores son 1, 2 y 3"
    print ("Los valores son {}, {} y {}".format(1,2,3))

    # Entre las llaves podemos poner la posición del parámetro. {2} es el tercer parámetro de format()
    # {0} es el primer parámetro de format.
    # saca "Los valores son 3, 2 y 1"
    print ("Los valores son {2}, {1} y {0}, {0}, {0}".format(1,2,3))
    
    print ("{pepe} y {juan}".format(juan=1, pepe=2))
    
    usuario = 'AGalvezE'
    arroba = '@'
    dominio = 'universidad.edu.co'
    correo = usuario + arroba+ dominio
    correo = correo.lower()
    print (correo)
    
    mensaje3 = 'Hola'
    mensaje3 += ' '
    mensaje3 += 'Mundo'
    print(mensaje3)
#operacionesCadenas()



def diccionarios ():
    diccionario = {"total": 55, "descuento": True, 15: "15"}
    print(diccionario)

    diccionarioEjemploExcel ={"nombre":5+2,"telefono":3363692, "edad":33, "ciudad":"Pereira"}
    print(diccionarioEjemploExcel)
    
    diccionario = dict(total= 55, descuento= True, subtotal= 15)
    print(diccionario)
    
    diccionario = {"total": 55, 10: "Curso de Python", 2.0: True}
    print(diccionario)
    
    
    usuario = {
    'nombre': 'Nombre del usuario',
    'edad' : 23, 
    'curso': 'Curso de Python',
    'skills':{
            'programacion' : True,
            'base_de_datos': False
            },
    'No medallas' : 10
    }

    print(usuario)
    print(usuario['curso'])
    print(usuario['skills'])
    print(usuario['skills']['base_de_datos'])
    
    diccionario = dict(total=55, descuento=True, descuento5=True, subtotal="15")

    print(diccionario)
    print(diccionario['subtotal'])   
    
    
    diccionario = dict()
    print(diccionario)

    diccionario['marca'] = 'Mazda'
    print(diccionario['marca'])

    diccionario['marca'] = 'Subaru'
    print(diccionario['marca'])

    print(diccionario) 
    
    diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
    print(diccionario)
    
    print (diccionario.keys())
    
    print (diccionario.values())
    
    versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
    print (versiones['zope'])
diccionarios()


#3. Quedamos por Clase 10 ( Acceder a valor de clave )
#para la proxima sesión el dia lunes 17 de mayo
#la sesion se encuentra en la clase 7