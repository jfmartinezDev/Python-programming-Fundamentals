'''
Ejercicio 1: Escriba un programa en python para calcular la nota promedio a partir de tres notas leídas.
'''

def  notaPromedio ():
    print ("Por favor ingrese el valor de la nota 1: ")
    nota1 = float(input())
    nota2 = float (input ("Por favor ingrese el valor de la nota 2: "))
    nota3 = float (input("Por favor ingrese el valor de la nota 3: "))
    promedio = (nota1 + nota2 + nota3 ) / 3
    promedio = round(promedio,2)
    print ("La nota promedio es: "+str(promedio))
'''notaPromedio()
notaPromedio()
notaPromedio()'''


'''
Ejercicio 2: Escriba un programa en python para calcular la nota definitiva de tres notas leídas teniendo en cuenta la siguiente ponderación: La nota 1 vale 30%, la nota 2 vale 20% y la nota tres vale 50%.
'''

def notaFinal ():
    print ("Por favor ingrese la nota 1: ")
    nota1 = float(input())
    print ("Por favor ingrese la nota 2: ")
    nota2 = float(input())
    print ("Por favor ingrese la nota 3: ")
    nota3 = float(input())
    notaDefinitiva = nota1 * 0.3 + nota2 * 0.2 + nota3 * 0.5
    print (round (notaDefinitiva,2))
'''notaFinal()
notaFinal()
notaFinal()'''



'''
Ejercicio 3: Diseñar un algoritmo que lea dos valores reales y nos muestre los resultados de sumar, restar, dividir (el segundo número debe ser diferente de cero) y multiplicar dichos números.
'''
def operaciones ():
    x = float(input("Ingrese un valor para x: "))
    y = float(input("Ingrese un valor para y: "))
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    division = x / y
    print (str(x) + " + " + str(y) + " = " + str(suma))
    print (str(x) + " - " + str(y) + " = " + str(resta))
    print (str(x) + " * " + str(y) + " = " + str(multiplicacion))
    print (str(x) + " / " + str(y) + " = " + str(division))
'''operaciones ()
operaciones ()
operaciones ()'''


def operaciones1(x, y):
    x = float(x)
    y = float(y)
    suma =  x + y 
    resta = x - y 
    multiplicacion = x * y
    division = x / y
    division = round (division,2)
    print (str(x) + " + " + str(y) + " = " + str(suma))
    print (str(x) + " - " + str(y) + " = " + str(resta))
    print (str(x) + " * " + str(y) + " = " + str(multiplicacion))
    print (str(x) + " / " + str(y) + " = " + str(division))

'''operaciones1 (20.0, 50.0)       
operaciones1 (9, 3) 
operaciones1 (-1.0, -2.0) 
operaciones1 (0, 1) 
operaciones1 (3, -3) 
operaciones1 (50, 60) '''



def funcionSuma ( x , y):
    """
    La funcion realiza una suma de dos variables (x,y)
    x corresponde  a la primera variable
    y corresponde a la segunda variable
    """
    x = float(x)
    y = float(y)
    suma = x + y
    print (str(x) + " + " + str(y) + " = " + str(suma))

def funcionResta (x , y):
    """
    La funcion realiza una suma de dos variables (x,y)
    x (float) corresponde  a la primera variable
    y (float) corresponde a la segunda variable
    """
    x = float(x)
    y = float(y)
    resta = x - y
    print (str(x) + " - " + str(y) + " = " + str(resta))

def funcionMultiplicacion ( x, y):
    """
    La funcion realiza una resta de dos variables (x,y)
    x (float) corresponde  a la primera variable
    y (float) corresponde a la segunda variable
    """
    x = float(x)
    y = float(y)
    multiplicacion = x * y
    print (str(x) + " * " + str(y) + " = " + str(multiplicacion))   

def funcionDivision ( x, y):
    """
    La funcion realiza la division de dos variables (x,y)
    x (division) corresponde  a la primera variable
    y (division) corresponde a la segunda variable
    """
    x = float(x)
    y = float(y)
    division = x / y
    print (str(x) + " / " + str(y) + " = " + str(division)) 

'''funcionSuma ( 20, 30)
funcionResta (30, 50)
funcionSuma (10,20)
numero1 = float (input ("Por favor ingrese el numero 1: "))
numero2 = float (input ("Por favor ingrese el numero 2: "))
funcionDivision (numero1, numero2)'''



def funcionSuma2 (x, y):
    """
    La funcion realiza una suma de dos variables (x,y)
    x corresponde  a la primera variable
    y corresponde a la segunda variable
    """
    x = float(x)
    y = float(y)   
    suma = x + y
    salida = str(x) + " + " + str (y) + " = " + str (suma) 
    return salida

'''resultado = funcionSuma2 ( 20, 30)
print (resultado)'''