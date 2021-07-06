def conversion():
    cadena = 'abcdefgaaabbccd'
    print ('cadena  =  ', cadena)
    
    lista = list(cadena)
    print ('lista = ', lista)
    #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'd']
    
    tupla = tuple (cadena)
    print ('tupla = ', tupla)
    #('a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'd')
    
    conjunto = set (cadena)
    print ('conjunto = ',conjunto)
    # {'c', 'a', 'e', 'g', 'f', 'b', 'd'}
conversion() 
    



def conversionListas():
    lista = ['a','b', 'c', 'd']
    print ('lista = ', lista)
      
    tupla = tuple (lista)
    print ('tupla = ', tupla)
    
    texto = str(lista)
    print ('texto = ', texto) # ['a', 'b', 'c', 'd']
    texto = ''.join (lista)
    print ('texto = ', texto) # abcd
    
conversionListas()

def conversionTupla ():
    tupla = ('a', 'b', 'c', 'd')
    print ('tupla = ', tupla)
    
      lista = list (tupla)
      print ('lista = ', lista) #['a', 'b', 'c', 'd']
      
      conjunto = set (tupla)
      print ('conjunto = ', conjunto) #{'a', 'c', 'b', 'd'}
      
      texto = ''.join(tupla) 
      print ('texto = ', texto) #abcd
      
  conversionTupla()


  def conversionConjunto():
      conjunto = {'a', 'b', 'c', 'd', 'a', 'b'}
      print ('conjunto = ', conjunto)
      
      lista = list(conjunto)
      print (lista) #['b', 'a', 'c', 'd']
      
      tupla = tuple(conjunto)
      print (tupla) #('b', 'a', 'c', 'd')
      
      texto = ''.join(conjunto)
      print (texto) #bacd

  conversionConjunto()


  def conversionDiccionario():
      listaLLaves = ['a', 'b', 'c', 'd']
      listaValores = [50,60,70,90]
      
      listaNueva = list (zip(listaLLaves,listaValores))
      
      tuplaNueva = tuple (zip(listaLLaves,listaValores))
      
      diccionario = dict (zip(listaLLaves,listaValores))
      
      print ('listaNueva = ', listaNueva)
      print ('tuplaNueva = ', tuplaNueva)
      print ('diccionario = ', diccionario)
      

      
  conversionDiccionario()

  #conversionDiccionario()

  def conversionDiccionarioTo ():
      diccionario = {0:'h', 1:'o', 2:'l', 3:'a'}
      
      dicToTexto = ''.join ( diccionario.values() )
      print ('dicToTexto = ', dicToTexto) #hola
      
      texto = ''
      for clave, valor in diccionario.items():
          texto += str(clave) +' '
      print ('texto = ', texto)
      
      listaValores = list( diccionario.values() )
      print ('listaValores = ', listaValores) #['h', 'o', 'l', 'a']
      
      tuplaValores = tuple(diccionario.values() )
      print ('tuplaValores = ', tuplaValores) #('h', 'o', 'l', 'a')
      
      tuplaLlavesYValores = list (diccionario.items())
      print ('tuplaLlavesYValores = ', tuplaLlavesYValores) #[(0, 'h'), (1, 'o'), (2, 'l'), (3, 'a')]
      
  conversionDiccionarioTo()