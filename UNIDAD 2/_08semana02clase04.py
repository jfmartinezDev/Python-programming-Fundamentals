#lunes
'''
Escriba las expresiones equivalentes a las siguientes proposiciones en español, usando los 3 identificadores P, Q y R.

P: Hoy es martes
Q: Hoy está haciendo calor
R: Es un dia de fiesta

Hoy no es martes
¬P

Hoy no es martes o hoy es martes
¬P v P

Hoy está haciendo calor o es martes o es un día de fiesta
Q v P v R

Hoy ni es martes ni es un día de fiesta
¬P ^ ¬R


'''


def teoria1():
  x = 10
  if x > 0 :
      print('x es positivo')
teoria1()

def teoria2():
  x = 40.0
  y = x
  print (x != y) # x no es igual a y
  print (x > y) # x es mayor que y
  print (x < y) # x es menor que y
  print (x >= y) # x es mayor o igual que y
  print (x <= y) # x es menor o igual que y
  print ("x is y ¿", x, " es lo mismo que ", y , "? ",  x is y) # x es lo mismo que y
  print (x is not y) # x no es lo mismo que y
teoria2()