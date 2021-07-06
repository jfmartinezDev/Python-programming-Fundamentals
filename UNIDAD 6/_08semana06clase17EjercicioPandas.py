# Ejercicio:
# Dado un DataFrame con la siguiente información: 6 columnas: ‘nombre’, donde aparecen los nombres de los estudiantes, ‘matemáticas’, ‘inglés’, ‘ciencias’, ‘literatura’ y ‘arte’, en las cuales aparecen las calificaciones de los estudiantes en cada una de esas materias. Las calificaciones son números decimales entre 0 y 5.0.
# Construya una función que reciba un DataFrame con información sobre el desempeño de un conjunto de estudiantes en 5 materias y retorne un diccionario con las siguientes llaves:
# -	'ordenado', el valor es una tupla nombre, promedio ordenado de forma descendente (mayor a menor)
# -	'mejorPromedio', el valor es un diccionario {nombre : promedio} con el (los) nombre (s) de los estudiantes con el mejor promedio
# -	'promedioSupA4', el valor es un diccionario {nombre : promedio} con el (los) nombre (s) de los estudiantes con los promedios superiores a 4.0
# -	'promedioDeTodos', el valor es el promedio de todos los estudiantes en general.

# Ejemplo:

# def mejores_estudiantes(estudiantes: pd.DataFrame)-> dict:
#     pass

import pandas as pd


def mejores_estudiantes(estudiantes: pd.DataFrame)-> dict:
    
    diccionario = dict ()
    # Primer punto (Promedio de cada fila) mean = media artimética
    estudiantes ['promedio'] = round (  (estudiantes.mean (axis = 1) ), 3)
    # print (estudiantes)
    # Procedemos a ordenar estos datos de manera descendente, el promedio
    salida1 = estudiantes.sort_values ( by = ['promedio'], ascending=False, ignore_index=True  )
    # print (salida1) 
    
    # Segundo punto (Nombre de las personas con mejor promedio), se calcula con la función max
    mayorPromedio = max (salida1['promedio'])
    # print ('El mayor promedio es: ', mayorPromedio)
    salida2 = salida1.loc [ salida1 ['promedio'] == mayorPromedio ]
    # print (salida2)
    
    # Tercer punto (Nombre de las personas con promedioSupA4)
    salida3 = salida1.loc [ salida1 ['promedio'] > 4.0 ]

    # Cuarto punto Promedio de todos
    suma = sum (salida1['promedio'])
    promedio = round   (   (suma / len (salida1['promedio'])), 3)
    
    diccionario['ordenado'] = tuple ( zip (salida1['nombre'], salida1['promedio']) )
    diccionario['mejorPromedio'] =  dict ( zip (salida2['nombre'], salida2['promedio']) )
    diccionario['promedioSupA4'] = dict ( zip (salida3['nombre'],  salida3['promedio']) )
    diccionario['promedioDeTodos'] = promedio
    
    return diccionario




# Data frame de los estudiantes
estudiantes ={'nombre':['susana','luis','ana','tati','juan'], 
              'matematicas':[2.5,3.5,4.5,5.0,3.897], 
              'ingles':[0.5,1.0,5.0,4.8,5.0], 
              'ciencias':[5.0,4.0,4.6,5.0,4.0], 
              'literatura':[4.5,5.0,3.8,4.5,5.0], 
              'arte':[4.5,5.0,4.5,1.0,5.0]
            }
df = pd.DataFrame (estudiantes,columns = ['nombre','matematicas','ingles','ciencias','literatura','arte'])
#print ('dataFrame = \n', df)
print (mejores_estudiantes(df))

# Desde otro archivo este es el enlace https://replit.com/@pyplusplusMF/grupo8Pandas#main.py


# https://www.youtube.com/c/DotCSV/videos