def listaDeListas ():
    matriz = [ [0 for j in range (3)] for i in range (4)]
    print (matriz)
    for i in range (4):
        for j in range (3):
            print (matriz[i][j], end = ' ')
        print ('')
    matriz[2][0] = -1
    matriz[2][2] = 9
    try:
        matriz[2][3] = 8 #IndexError 
    except:
        print ('Alguna posicion no es correcta')

    linea = '*'*7
    print (linea)
    for i in range (4):
        for j in range (3):
            print (matriz[i][j], end = ' ')
        print ('')

#listaDeListas()


def teoriaConjuntos():
    s = {True, 3.14, None, False, "Hola mundo", (1, 2)}
    print (s)
    s = { 3.14, False, 'Hoola',5.1, (1, 2),True, None, 5.10, 6.32, 'Hola2'}
    print (s)
    #Los conjuntos son aleatorios

    s1 = set([1, 2, 3, 4])
    s2 = set(range(10))
    print(s1)
    print(s2)   

    x = set([1, 2, 2, 3, 4, 3,3,3,3,3,3])
    print (x)

    a = set('Hola Pythonista')
    print(a)
    lista = list (a)
    print (lista)
    
    unicos = set([3, 5, 6, 1, 5,3,3,3,3,3,3,3,3,3,3,3,5,5,5,5])
    print(unicos)

    mi_conjunto = {1, 3, 2, 9, 3, 1}
    print(mi_conjunto)
    for numero in mi_conjunto:
        print(numero)

    conjunto = set ()
    for i in range (5):
        elemento = int(input('Ingrese un elemento: '))
        conjunto.add (elemento)
    print (conjunto)
    '''
    Ingrese un elemento: 5
    Ingrese un elemento: 2
    Ingrese un elemento: -1
    Ingrese un elemento: -1
    Ingrese un elemento: 5
    {2, 5, -1}
    '''      

teoriaConjuntos()


def operacionesConjuntos ():
        
    A = {1,2,3,4,5,6,7,8,9,10}
    B = {0,1,3,5,7,9,11,13,15,17}
    #Union
    AuB = A.union (B)
    AuB2 = A | B
    print ('AuB = ', AuB)
    print ('AuB2 = ', AuB2)
    #Interseccion
    AnB = A.intersection (B)
    AnB2 = A & B
    print ('AnB = ', AnB)
    print ('AnB2 = ', AnB2)
    
    #Diferencia
    A_B = A.difference(B)
    A_B2 = A - B
    print ('A - B = ', A_B)
    print ('A - B2 = ', A_B2)
    
    #Diferencia simétrica
    AdsB = A.symmetric_difference(B)
    AdsB2 = A ^ B
    print ('dif simetrica A B = ', AdsB)
    print ('dif simetrica A B = ', AdsB2)
    
operacionesConjuntos()



