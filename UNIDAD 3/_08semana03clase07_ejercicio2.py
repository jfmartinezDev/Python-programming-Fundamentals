def validacionNota4 (notas:dict) -> dict:
    """
    Parámetros:
        notas (dict): Diccionario que tiene tres claves: nota1, nota2, nota3
    
    Retorno:
        dict : diccionario con dos claves: promedio (float), informacion(str)
    """
    variableNota1 = float(notas['nota1'])
    variableNota2 = float(notas['nota2'])
    variableNota3 = float(notas['nota3'])

    #promedio = (variableNota1 + variableNota2 + variableNota3) / 3
    promedio = (sum(notas.values())) / len (notas)
    promedio = round (promedio,2)
    salida = ' '
    notasInvalidas = variableNota1 < 0.0 or variableNota2 < 0.0 or variableNota3 < 0.0 or variableNota1 > 5.0 or variableNota2 > 5.0 or variableNota3 > 5.0 
    
    if (notasInvalidas == True):
        salida = 'Notas Invalidas'
        promedio = 0
    elif(promedio >= 3.0):
        salida = 'Aprobó'
    elif(promedio < 3.0):
        salida = 'Reprobó'    
    
    diccionarioSalida = dict()
    diccionarioSalida['promedio'] = promedio
    diccionarioSalida['informacion'] = salida
    
    return diccionarioSalida



diccionarioNotas = {'nota1': 3.5, 'nota2': 5.0, 'nota3': 5.0}
print (validacionNota4(diccionarioNotas))

diccionarioNotas = {'nota1': -1, 'nota2': 5.0, 'nota3': 5.0}
print (validacionNota4(diccionarioNotas))


diccionario = dict()
x = float(input("Ingrese la nota 1: "))
y = float(input("Ingrese la nota 2: "))
z = float(input("Ingrese la nota 3: "))
diccionario ['nota1'] = x
diccionario ['nota2'] = y
diccionario ['nota3'] = z 
print (validacionNota4(diccionario))


diccionario = dict()
diccionario ['nota1'] = float(input("Ingrese la nota 1: "))
diccionario ['nota2'] = float(input("Ingrese la nota 2: "))
diccionario ['nota3'] = float(input("Ingrese la nota 3: ")) 
print (validacionNota4(diccionario))


###El dia de mañana martes 18 de mayo comenzamos ciclos y listas