def diccionarios2():
  versiones = dict(python=2.7, zope=2.13, plone=5.1)
  print(versiones)
  versiones.clear()
  print(versiones)
  
  
  versiones = dict(python=2.7, zope=2.13, plone=5.1)
  print ("versiones", versiones)
  otra_versiones = versiones.copy()
  print ("otra_versiones", otra_versiones)
  print(versiones == otra_versiones)


  secuencia = ('python', 'zope', 'plone')
  versiones = dict.fromkeys(secuencia)
  print("Nuevo Diccionario : %s" %  str(versiones))
  print("Nuevo Diccionario : {}".format(str(versiones)))

  secuencia = ('python', 'zope', 'plone')
  versiones = dict.fromkeys(secuencia, 0.1)
  print("Nuevo Diccionario : %s" %  str(versiones))

  versiones = dict(python=2.7, zope=2.13, plone=5.1)
  print ("versiones", versiones)
  print (versiones.get('plone'))
  print (versiones.get('php')) #el resultado sera None


  versiones = dict(python=2.7, zope=2.13, plone=5.1)
  print ("versiones", versiones)
  print (versiones.items())
  

  versiones = dict(python=2.7, zope=2.13, plone=5.1)
  print (versiones)
  print (versiones.pop('zope'))
  print (versiones)

  versiones = dict(python=2.7, zope=2.13, plone=5.1)
  print(versiones)
  versiones_adicional = dict(django=2.1)
  print(versiones_adicional)
  versiones.update(versiones_adicional)
  print(versiones)
  versiones_adicional = dict(python = 3.9)
  print (versiones_adicional)
  versiones.update(versiones_adicional)
  print (versiones)


  versiones = dict(python=2.7, zope=2.13, plone=5.1)
  print (versiones)
  print (len(versiones))

  usuario = {
      'nombre': 'Nombre del usuario',
      'edad' : 23, 
      'curso': 'Curso de Python',
      'skills':{
          'programacion' : True,
          'base_de_datos': False
      },
      'No medallas' : 10
  }
  print("La cantidad de llaves de primer nivel son: ", len(usuario))
  print ("La cantidad de llaves de segundo nivel de la clave skills son: ", len(usuario['skills']))

  versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
  print(versiones)
  del versiones["python"] #{'zope': 2.13, 'plone': 5.1, 'django': 2.1}
  print(versiones)
  #del versiones["Java"] sino se encuentra keyError
  
diccionarios2()

def diccionarios3():
  Estudiantes = {  'Alumno1': {'nombre':'Daniel', 'edad':11, 'estatura':1.75, 'grado':'Master'},
                 'Alumno2':{'nombre':'Valentina', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}   
              }

  #print(Estudiantes)
  print (Estudiantes ['Alumno1']['nombre'])
  print (Estudiantes ['Alumno2']['nombre'])

  if Estudiantes['Alumno1']['nombre'] == Estudiantes['Alumno2']['nombre']:
    print("Los nombres son iguales")
  else:
    print('Los nombres son diferentes')

  Informacion = {  'Alumno1': {'nombre':'Daniel', 'edad':21, 'estatura':1.75, 'grado':'Master'},
                 'Alumno2':{'nombre':'Valentina', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}   }

  if Informacion['Alumno1']['edad'] > Informacion['Alumno2']['edad']:
      
      print(str(Informacion['Alumno1']['nombre']) + ' es mayor') 
      mayor = {'nombremayor':Informacion['Alumno1']['nombre'], 'edadmayor':Informacion['Alumno1']['edad'] }
      
  elif Informacion['Alumno1']['edad'] < Informacion['Alumno2']['edad']:
      
      print(str(Informacion['Alumno1']['nombre']) + ' es menor') 
      
      mayor = {'nombremayor':Informacion['Alumno2']['nombre'], 'edadmayor':Informacion['Alumno2']['edad'] }
  print(mayor)
diccionarios3()
