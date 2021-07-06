#https://stackoverflow.com/questions/9987483/elif-in-list-comprehension-conditionals

#Enlace de interes de los paradigmas de programación
#https://youtu.be/V4vjB3vQGBY

def ejemplo1():
    #La funcion suma, recibe dos argumentos
    def funcionSuma (valor1 = 0, valor2 = 0):
        return valor1 + valor2

    #La funcion operacion, recibe una funcion(?) y dos valores
    #la funcion(?) es una funcion que no se sabe cual es
    def operacion (funcionX, valor1 = 0, valor2 = 0):
        #aqui se retorna la funcion(?) que se paso como parametro
        #y se pasan los dos argumentos valor1 y valor2
        return (funcionX (valor1, valor2))

    #aqui la variable resultado contiene el resultado de la funcion operacion
    #operacion recibe como argumento una funcion(?) y dos valores
    resultado = operacion (funcionSuma, 10, 20)
    print ('resultado = ', resultado)
    
# ejemplo1()

def ejemplo2():
    #Ejemplo 2
    #funcion que crea funciones a partir de un operador de tipo caracter
    def crearFuncion(operador:str):
        if (operador == '+'):
            def suma (valor1 = 0, valor2 = 0):
                return valor1 + valor2
            return suma
        elif (operador == '-'):
            def resta (valor1 = 0, valor2 = 0):
                return valor1 - valor2
            return resta
        elif (operador == '*'):
            def multiplicacion (valor1 = 0, valor2 = 0):
                return valor1 * valor2
            return multiplicacion
        elif (operador == '/'):
            def division (valor1 = 0, valor2 = 0):
                return valor1 / valor2
            return division     

    def operacion (funcion, valor1 =0, valor2 = 0):
        return ( funcion (valor1, valor2) )

    funcionSuma = crearFuncion('+')
    funcionResta = crearFuncion('-')
    funcionMultiplicacion = crearFuncion ('*')
    funcionDivision = crearFuncion ('/')
    
    resultado1 = operacion (funcionSuma, 10, 20)
    print ('resultado suma = ', resultado1)
    
    resultado2 = operacion (funcionResta, 10, 20)
    print ('resultado resta = ', resultado2)

    resultado3 = operacion (funcionMultiplicacion, 10, 20)
    print ('resultado multiplicacion = ', resultado3)
    
    resultado4 = operacion (funcionDivision, 10, 20)
    print ('resultado division = ', resultado4)

# ejemplo2()
def ejemplo3Lambda ():
    
    def funcionSuma (valor1 = 0, valor2 = 0):
        return valor1 + valor2
    def operacion (funcionX, valor1 = 0, valor2 = 0):
        return (funcionX (valor1, valor2))
    resultado1 = operacion (funcionSuma, 10, 20)
    print ('resultado1 = ', resultado1)   
    
    #Todo en una linea...No se debe abusar de lambda.. El codigo se hará dificil de comprender
    funcionSuma = lambda valor1 = 0, valor2 = 0: valor1 + valor2
    operacion = lambda funcionX, valor1 = 0, valor2 = 0: (funcionX (valor1, valor2))
    resultado2 = operacion (funcionSuma, 10, 20)
    print ('resultado2 = ', resultado2)
    
#ejemplo3Lambda()

def ejercicio1Lambda():
    #ejercicio con lambda
    #Funcion para el cuadrado de un numero
    def cuadrado (x):
        return x**2
    print ('funcioncuadrado = ',cuadrado(4))

    funcionCuadrado = lambda x : x * x
    print ('lambda = ', funcionCuadrado(4))
# ejercicio1Lambda()

def ejercicio2Lambda():
    #Ejercicio con lambda
    #funcion que calcula la multiplicacion de dos numeros
    def multi (x, y):
        return x * y
    print ('multi ', multi(3,4))
    
    funcionMulti = lambda x,y : x * y
    print ('lambda = ', funcionMulti(3,4))
# ejercicio2Lambda()

def ejercicio3Lambda():
    #Ejercicio con lambda y condicionales
    mayor = lambda x,y: x if x > y else y
    print ( 'Mayor = ', mayor (40, 1))
# ejercicio3Lambda()

def ejercicio4Lambda():
    #Ejercicio con lambda retornando un lambda
    #retorna una funcion lambda de otra funcion
    def funcion (valor):
        return lambda x : x * valor

    var1 = funcion (2) #aqui var1 llama a la funcion
    #resulta que var1 retorna el equivalente de 
    #lambda x : x * 2, 5 * 2
    var1 = var1 (5) #por eso toma el valor de 10
    print ('var1 = ',var1)
    
    var2 = funcion (3) #aqui var2 llama a la funcion
    #resulta que var2 retorna el equivalente de 
    #lambda x : x * 2, 5 * 3
    var2 = var2 (5) #por eso toma el valor de 15
    print ('var2 = ',var2)
ejercicio4Lambda()


def ejercicio5LambdaConDiccionarios():
    # Transformar los valores de un diccionario a su cuadrado
    # #ejemplo { 'a': 2...} retorna { 'a': 4}
    
    # con los ciclos de un dict
    diccionario = {'a': 1, 'b':2, 'c':3}
    print ('diccionario antes: ', diccionario)
    for clave, valor in diccionario.items():
        diccionario[clave] = valor * valor
    print ('diccionario despues: ', diccionario)
    
    print('-'*50)
    # con comprension de diccionarios
    diccionario2 = {'a': 1, 'b':2, 'c':3}
    print ('diccionario2 antes: ', diccionario2)
    diccionario2 = {clave : valor * valor
                    for clave, valor in diccionario2.items()}
    print ('diccionario2 despues: ', diccionario2)
    
    print('-'*50)
    # con lambda paso por paso
    def transformarValores (funcionLambda, diccionario):
        return {clave: funcionLambda(valor)
                for clave, valor in diccionario.items()}
    
    diccionario3 = {'a': 1, 'b':2, 'c':3}
    print ('diccionario3 antes: ', diccionario3)
    
    funcionLambda = lambda x: x * x #funcion que eleva al cuadrado
    diccionario3 = transformarValores (funcionLambda, diccionario3)
    print ('diccionario3 despues: ', diccionario3)
    print('-'*50)
    diccionario4 = {'A': 1, 'B':2, 'C':3}
    print ('diccionario4 antes: ', diccionario4)

    funcionLambda2 = lambda x: x ** 3
    diccionario4 = transformarValores (funcionLambda2, diccionario4)
    print ('diccionario4 despues: ', diccionario4)
    

ejercicio5LambdaConDiccionarios()





