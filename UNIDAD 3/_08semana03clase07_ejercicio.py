'''
Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y
5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó
o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro
del rango permitido
'''

def validarNota1 (notas:dict) -> str:
    """
    Parámetros:
        notas (dict): Diccionario que tiene tres claves: nota1, nota2, nota3
    
    Retorno:
        str : Indicar si la nota promedio es aprobatoria, reprobatoria, No valida
    """
    variableNota1 = float(notas['nota1'])
    variableNota2 = float(notas['nota2'])
    variableNota3 = float(notas['nota3'])

    promedio = (variableNota1 + variableNota2 + variableNota3) / 3
    salida = ' '
    notasInvalidas = variableNota1 < 0.0 or variableNota2 < 0.0 or variableNota3 < 0.0 or variableNota1 > 5.0 or variableNota2 > 5.0 or variableNota3 > 5.0 
    
    if (notasInvalidas == True):
        salida = 'Notas Invalidas'
    else:
        if (promedio >= 3.0):
            salida = 'Aprobó'
        else:
            if (promedio < 3.0):
                salida = 'Reprobó'
    
    return salida


'''diccionarioNotas = {'nota1': 3.5, 'nota2': 5.0, 'nota3': 5.0}
print (validarNota1(diccionarioNotas))

diccionarioNotas = {'nota1': -1, 'nota2': 5.0, 'nota3': 5.0}
print (validarNota1(diccionarioNotas))


diccionario = dict()
x = float(input("Ingrese la nota 1: "))
y = float(input("Ingrese la nota 2: "))
z = float(input("Ingrese la nota 3: "))
diccionario ['nota1'] = x
diccionario ['nota2'] = y
diccionario ['nota3'] = z 
print (validarNota1(diccionario))


diccionario = dict()
diccionario ['nota1'] = float(input("Ingrese la nota 1: "))
diccionario ['nota2'] = float(input("Ingrese la nota 2: "))
diccionario ['nota3'] = float(input("Ingrese la nota 3: ")) 
print (validarNota1(diccionario))
'''


def validarNota2 (notas:dict) -> str:
    """
    Parámetros:
        notas (dict): Diccionario que tiene tres claves: nota1, nota2, nota3
    
    Retorno:
        str : Indicar si la nota promedio es aprobatoria, reprobatoria, No valida
    """   
    promedio  =    sum (notas.values())  / 3
    promedio = round (promedio, 2)
    
    #promedio = (notas['nota1'] + notas['nota2'] + notas['nota3']) / 3
    salida = ' '
    notasInvalidas = notas['nota1'] < 0.0 or notas['nota2']< 0.0 or notas['nota3'] < 0.0 or notas['nota1'] > 5.0 or notas['nota2'] > 5.0 or notas['nota3'] > 5.0 
    notaAprobatoria = promedio >= 3.0
    notaReprobatoria = promedio < 3.0
    
    if (notasInvalidas):
        salida = 'Notas Invalidas'
    elif (notaAprobatoria):
        salida = 'Aprobó'
    elif (notaReprobatoria):
        salida = 'Reprobó'
    
    return salida


diccionarioNotas = {'nota1': 3.5, 'nota2': 5.0, 'nota3': 5.0}
print (validarNota2(diccionarioNotas))

diccionarioNotas = {'nota1': -1, 'nota2': 5.0, 'nota3': 5.0}
print (validarNota2(diccionarioNotas))


diccionario = dict()
x = float(input("Ingrese la nota 1: "))
y = float(input("Ingrese la nota 2: "))
z = float(input("Ingrese la nota 3: "))
diccionario ['nota1'] = x
diccionario ['nota2'] = y
diccionario ['nota3'] = z 
print (validarNota2(diccionario))


diccionario = dict()
diccionario ['nota1'] = float(input("Ingrese la nota 1: "))
diccionario ['nota2'] = float(input("Ingrese la nota 2: "))
diccionario ['nota3'] = float(input("Ingrese la nota 3: ")) 
print (validarNota2(diccionario))