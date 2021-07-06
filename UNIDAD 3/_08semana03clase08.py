def cicloWhile():
    n = 5
    while n > 0:
        print(n)
        n = n - 1
    print('Despegue!')
cicloWhile()

def factorial (n:int) -> int:
    i = 1
    factorial = 1
    while ( i<= n):
        factorial = factorial * i
        i = i + 1
    return factorial
print (factorial (0))
print (factorial (6))


def cicloControladoPorEvento():
    promedio, total, contar = 0.0, 0, 0

    print("Introduzca la nota de un estudiante (-1 para salir): ")
    grado = int(input())
    while grado != -1:
        total = total + grado
        contar = contar + 1
        print("Introduzca la nota de un estudiante (-1 para salir): ")
        grado = int(input())
    promedio = total / contar
    print("Promedio de notas del grado escolar es: " + str(promedio))
cicloControladoPorEvento()


def cicloWhileConElse():
    promedio, total, contar = 0.0, 0, 0
    mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

    grado = int(input(mensaje))
    while grado != -1:
        total = total + grado
        contar += 1
        grado = int(input(mensaje))
    else:
        promedio = total / contar
        print("Promedio de notas del grado escolar: " + str(promedio))
cicloWhileConElse()

def cicloBreak():
    variable = 10

    while variable > 0:
        print('Actual valor de variable:', variable)
        variable = variable -1
        if variable == 5:
            break
cicloBreak()

def cicloContinue():
    variable = 10

    while variable > 0:
        variable = variable -1
        if variable == 5:
            continue
        print('Actual valor de variable:', variable) # no imprime el 5
cicloContinue()

def factorialConFor(n:int) -> int:
    factorial = 1 
    for i in range (1,n+1):
        factorial *= i
    return factorial
print (factorialConFor(0))
print (factorialConFor(3))


def ciclofor():
    for j in range(0, 10, 2):
        print("Estamos en la iteración " + str(j))
ciclofor()



def ciclofor2():
    for j in range(10, 0, -2):
        print("Estamos en la iteración " + str(j))
ciclofor2()

#documentacion de python sobre el rango https://docs.python.org/3/library/stdtypes.html#typesseq-range


def cicloConstr():
    oracion = 'Mary entiende muy bien Python'
    frases = oracion.split() # convierte a una lista cada palabra
    print (frases)
    print("La oración analizada es:", oracion, ".\n")

    for posicion in range(len(frases)):
        print("Palabra: {0}, en la frase su posición es: {1}".format(
            frases[posicion], posicion))
cicloConstr()