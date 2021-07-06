print ("Hola mundo")
print ("Bienvenidos a MisionTIC y a la UTP")
print ("****Mi nombre es Maria F. Medina****")

var1 = 1.20
print(var1)

var1 = int(var1)
print (var1)

var1 = 120
var2 = 200

print(var1)
print(var2)

var1 = var2 = var3 = 200
print(var1)
print(var2)
print(var3)

var1, var2, var3 = 10 , 20 , 30
print(var1)
print(var2)
print(var3)

'''
Ejercicio 1: Escriba un programa en python para calcular la nota promedio a partir de tres notas leídas.
'''

print ("Por favor ingrese el valor de la nota 1: ")
nota1 = float(input())
nota2 = float (input ("Por favor ingrese el valor de la nota 2: "))
nota3 = float (input("Por favor ingrese el valor de la nota 3: "))
promedio = (nota1 + nota2 + nota3 ) / 3
promedio = round(promedio,2)
print ("La nota promedio es: "+str(promedio))

'''
Ejercicio 2: Escriba un programa en python para calcular la nota definitiva de tres notas leídas teniendo en cuenta la siguiente ponderación: La nota 1 vale 30%, la nota 2 vale 20% y la nota tres vale 50%.
'''

print ("Por favor ingrese la nota 1: ")
nota1 = float(input())
print ("Por favor ingrese la nota 2: ")
nota2 = float(input())
print ("Por favor ingrese la nota 3: ")
nota3 = float(input())
notaDefinitiva = nota1 * 0.3 + nota2 * 0.2 + nota3 * 0.5
print (round (notaDefinitiva,2))


'''
Ejercicio 3: Diseñar un algoritmo que lea dos valores reales y nos muestre los resultados de sumar, restar, dividir (el segundo número debe ser diferente de cero) y multiplicar dichos números.
'''




'''
Ejercicio 4: Leer la temperatura dada en la escala Celsius e imprimir en su equivalente Fahrenheit. La fórmula de conversión es
'''

