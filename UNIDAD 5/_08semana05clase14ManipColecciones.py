#Lunes 31 de mayo
#sintaxis de map
# map (funcionParaAplicar, objeto iterable)


def ejemploMap():
  #Transformar todos los elementos a su cuadrado
  # def conversionLista(lista):
  #   for i in range (len(lista)):
  #     lista[i] = lista[i] * lista[i]
  #   return lista

  # lista = [1,2,3,4,5,6,7,8,9,10]
  # print ('lista Original = ', lista)
  # print ('Lista convertida= ', conversionLista (lista))

  def cuadrado (elemento):
    return elemento * elemento
  lista = [1,2,3,4,5,6,7,8,9,10]
  print ('lista Original = ', lista)
  listaTransformada = list (map(cuadrado, lista))
  print ('Lista convertida= ', listaTransformada)
ejemploMap()