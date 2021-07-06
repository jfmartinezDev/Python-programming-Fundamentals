#Imprima los números del 4 al 30, de 2 en 2.
def ciclo1():
    start = 4
    stop = 31
    step = 2
    print ('ciclo 1: ')
    for i in range (start, stop, step):
        print (i, end = ' ')
        
    print ('\nciclo 2: ')
    for i in range (4,31,2):
        print (i, end = ' ')
    
    print ('\nCiclo 3: ')
    i = 4
    n = 30
    while ( i <= n):
        print (i, end = ' ')
        i += 2
    
    print ('\nCiclo 4: ')
    for i in range (31):
        if ( i >= 4 and i%2 == 0):
            print (i, end = ' ')
    
    print ('\nCiclo 5: ')
    i = 0
    n = 30
    while ( i <= n):
        if ( i >= 4 and i%2 == 0):
            print (i, end = ' ')
        i += 1
ciclo1()

def listas1():
    print ('\nLista : ')
    lista = []
    for i in range (4,31,2):
        lista.append (i)  
    print (lista)
listas1()

def listas2():
    #Cree una lista con cuadrados de los números, de dos en dos, 
    # del 4 al 30, que son divisibles entre 3
    print ('Lista con cuadrados de 2 en 2 del 4 al 30 divisib entre 3')
    lista = [] #list()
    for i in range (4,31,2):
        residuo = i%3
        if (residuo == 0):
            cuadrado = i**2
            lista.append (cuadrado)
    #print (lista)
    #Segunda forma:
    lista = []
    for i in range (4,31,2):
        if (i%3 == 0):
            lista.append (i**2)
    print (lista)
    #[36, 144, 324, 576, 900]
listas2()

def diccionario1():
    #Cree un diccionario en el que las llaves sean una tupla entre 
    # los números del 3 al 10 y su respectivo cubo.
    #Y dónde los valores sean las listas con los cuadrados de 
    # los números de dos en dos, entre el 4 y el 30,
    #que son divisibles enteros con el primer elemento de su llave correspondiente.

    diccionario = dict()
    for i in range(3, 11):
        llave = (i, i**3)
        diccionario[llave] = []
        for j in range(4, 31, 2):
            if j%i == 0:
                diccionario[llave].append(j**2)
    print (diccionario)
    
diccionario1()


def diccionario2():
    mi_diccionario = dict()
    for y in range(3, 11): #ciclo externo
        mi_diccionario[(y, y**3)] = []
        for x in range(4, 31, 2): #ciclo interno
            if x%y == 0:
                mi_diccionario[(y, y**3)].append(x**2)

    print(mi_diccionario)
                        #llaves      #valor      #ciclo interno  #condicional      #ciclo externo
    mi_diccionario = { (y, y**3) : [ x**2 for x in range(4,31,2) if x%y == 0 ] for y in range(3, 11) }
                                #estos corchetes indican que se está creando lista
    print(mi_diccionario)
    
    
diccionario2()

def ciclo2():
    #Imprima los números del 4 al 30, de 2 en 2.
    lista = [x for x in range(4, 31, 2)]
    print (lista)
    #[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    
    lista2 = [0 for x in range (4,31,2)]
    print (lista2)
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    lista3 = [x for x in range(0, 31, 3)]
    print (lista3)
    #[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    
                       #ciclo interno        #ciclo externo
    listaDeListas = [[0 for j in range (3)] for i in range (5)]
    print (listaDeListas)
    #[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range (5): #ciclo externo
        for j in range (3): #ciclo interno
            print (listaDeListas[i][j], end = ' ')
        print (' ')
    '''
    0 0 0
    0 0 0
    0 0 0
    0 0 0
    0 0 0  
    '''  
            #elementos #ciclo externo       #condicional
    lista4 = [x**2 for x in range(4, 31, 2) if x%3 == 0] 
    print ('lista4 = ', lista4)
    
    conjunto = { i for i in range (1,21)}
    print ('conjunto = ', conjunto)

ciclo2()



