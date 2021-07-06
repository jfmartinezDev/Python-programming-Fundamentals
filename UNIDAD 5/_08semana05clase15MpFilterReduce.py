# Sesion del dia martes 1 de Junio
# Martes 1 de Junio
# Map Filter Reduce

# Sintaxis de map
# map (funcionParaAplicar, objeto iterable)

import functools


def ejemploMap():
  #Transformar todos los elementos a su cuadrado
  # def conversionLista(lista):
  #   for i in range (len(lista)):
  #     lista[i] = lista[i] * lista[i]
  #   return lista

  # lista = [1,2,3,4,5,6,7,8,9,10]
  # print ('lista Original = ', lista)
  # print ('Lista convertida= ', conversionLista (lista))

#   def cuadrado (elemento):
#     return elemento * elemento
#   lista = [1,2,3,4,5,6,7,8,9,10]
#   print ('lista Original = ', lista)
#   listaTransformada = list (map(cuadrado, lista))
#   print ('Lista convertida= ', listaTransformada)
  
  lista = [1,2,3,4,5,6,7,8,9,10]
  print ('lista Original = ', lista)
  funcionLambda = lambda elemento : elemento * elemento
  listaDeCuadrados = list (map (lambda elemento : elemento * elemento, lista))
  print ('Lista de cuadradps = ', listaDeCuadrados)
ejemploMap()

def ejemplo2Map():
    # pow (x,y)
    listaNumeros = [2,3,4]
    listaPotencia = [3,2,4]
    listaResultado = list (map(pow, listaNumeros, listaPotencia))
    print ('listaResultado = ', listaResultado)
    # [8, 9, 256]
ejemplo2Map()


def ejemploFilter():
    # Ejemplo, obtener la cantidad de elementos mayor a 5 en la tupla

    def mayorACinco (elemento):
        return elemento > 5

    tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
    resultado = list (filter (mayorACinco, tupla))
    print (resultado)
    print ('cantidad de elementos: ', len(resultado))
ejemploFilter()

def ejemplo2Filter():
    tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
    funcionLambda = lambda elemento: elemento > 5
    resultado = list (filter (funcionLambda, tupla))
ejemploFilter()

def ejemploFilter2():
    tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
    listaPares = []
    funcionLambda = lambda elemento: elemento % 2 == 0
    resultado = list (filter (funcionLambda, tupla))
    print ('resultado' , resultado)
    #resultado [2, 6, 8, 10, 2, 30, 4, 2]
ejemploFilter2()

from functools import reduce
def ejemploReduce ():
    # lambda con Reduce
    # aplicar la sumatora usando lambda
    lista = [1,2,3,4]
    resultado = (reduce (lambda acumulador = 0, elemento = 0: acumulador + elemento, lista))
    print (resultado)
ejemploReduce()

def ejemploReduce2():
    # Concatenar todos los elementos de una lista

    from functools import reduce

    lista = ['Python', 'Java', 'Ruby', 'Elixir']
    funcionLambda = lambda sumatoria = '', elemento = '': sumatoria + '-' + elemento
    resultado = reduce (  funcionLambda, lista  )
    print (resultado)
    # Python-Java-Ruby-Elixir
ejemploReduce2()

def ejemploReduce3():
    # Sumar 10 a cada elemento de la lista
    lista = [ 1,2,3,4,5,6,7,8,9]
    funcionLambda = lambda elemento1, elemento2: elemento1 + elemento2
    sumatoria= reduce (funcionLambda, lista, 10)
    print ( 'sumatoria = ', sumatoria)
ejemploReduce3()