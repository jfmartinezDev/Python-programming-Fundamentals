#martes
'''
Diseñe una funcion que reciba como parámetro un número real que represente la calificación 
numérica de un examen y retorne la calificación cualitativa correspondiente al número dado. 
La calificación cualitativa será una de las siguientes:
    0.0 a 2.9 Deficiente
    3.0 a 3.4 Regular
    3.5 a 3.9 Aceptable
    4.0 a 4.4 Bueno
    4.5 a 5.0 Excelente
'''
#1. No ingresar la nota dentro de la funcion
#2. En la funcion solo se evaluará la nota y se retornará una palabra
def notaCualitativa (nota:float) -> str:
    retorno = ""
    if (nota >= 0.0 and nota <= 2.9):
        retorno = "Deficiente"
    else:
        if (nota >= 3.0 and nota <= 3.4):
            retorno = "Regular"
        else:
            if (nota >= 3.5 and nota <= 3.9):
                retorno = "Aceptable"
            else:
                if (nota >= 4.0 and nota <= 4.4):
                    retorno = "Bueno"
                else:
                    if (nota >= 4.5 and nota <= 5.0):
                        retorno = "Excelente"
    return retorno

def notaCualitativa2 (nota:float) -> str:
    retorno = ""
    categoria1 = nota >= 0.0 and nota <= 2.9
    categoria2 = nota >= 3.0 and nota <= 3.4
    categoria3 = nota >= 3.5 and nota <= 3.9
    categoria4 = nota >= 4.0 and nota <= 4.4
    categoria5 = nota >= 4.5 and nota <= 5.0
    categoriaInvalida = nota < 0.0 or nota > 5.0
    
    if (categoria1):
        retorno = "Deficiente" 
    elif (categoria2):
        retorno = "Regular"
    elif (categoria3):
        retorno = "Aceptable"
    elif (categoria4):
        retorno = "Bueno"
    elif (categoria5):
        retorno = "Excelente"
    elif (categoriaInvalida):
        retorno = "No disponible"
    
    return retorno   


def notaCualitativa3 (nota:float) -> str:
    retorno = ""
    resultado = ""
    categoria1 = nota >= 0.0 and nota <= 2.9
    categoria2 = nota >= 3.0 and nota <= 3.4
    categoria3 = nota >= 3.5 and nota <= 3.9
    categoria4 = nota >= 4.0 and nota <= 4.4
    categoria5 = nota >= 4.5 and nota <= 5.0
    categoriaInvalida = nota < 0.0 or nota > 5.0
    
    #¿Como podría imprimir un mensaje indicando que la nota es aprobatoria? >= 3.0 y <= 5.0
    if (categoria2 or categoria3 or categoria4 or categoria5):
        resultado = "Aprobatoria"
    elif (categoria1):
        resultado = "Reprobatoria"
    elif (categoriaInvalida):
        resultado = "No disponible"
    
    if (categoria1):
        retorno = "Deficiente" 
    elif (categoria2):
        retorno = "Regular"
    elif (categoria3):
        retorno = "Aceptable"
    elif (categoria4):
        retorno = "Bueno"
    elif (categoria5):
        retorno = "Excelente"
    elif (categoriaInvalida):
        retorno = "No disponible"
    
    salida = "La nota es: " + str(resultado) + " y se encuentra en la categoria de "+str(retorno)
    return salida   

#calificacion = float(input("Digite la calificación: ")) 
#print(notaCualitativa(calificacion))            
#print(notaCualitativa2(calificacion))  
#print (notaCualitativa3(calificacion))



def cadenasTexto():
  #https://elcodigoascii.com.ar/

  fruta = "banana"
  longitud = len(fruta) #tamaño de la variable fruta
  print (longitud) #se imprime el tamaño de la fruta
  #ultimo = fruta[longitud] #saldra un error porque la fruta contiene longitud -1
  ultimo = fruta[longitud-1]
  print (ultimo)
  
  s = 'Monty Python'
  print(s[0:5])

  print ('z' in 'banana')
  print ("ban" in "banana")

  if ('d' > 'D'):
    print ("la letra d es mayor que la letra D")
  if ('z' > 'Z'):
      print ("la letra z es mayor que la letra Z")
cadenasTexto() 