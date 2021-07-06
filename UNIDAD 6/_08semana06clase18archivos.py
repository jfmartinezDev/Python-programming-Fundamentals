def pandas ():
  import pandas as pd

  data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
          'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
          'age': [27, 31, 36, 53, 48, 36, 40, 34],
          'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
          'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

  datosDataFrame = pd.DataFrame(data)

  print(datosDataFrame)

  #Acaba la implementacion

  datosDataFrame.to_csv('example.csv')


def archivoTXT():

  listaDeDatos = ['linea1', 'linea2', 'linea3', 'linea4']
  fic = open("text_1.txt", "w") 
  # se abre el archivo para escribir sobre el

  for line in listaDeDatos:
      fic.write(line)
      fic.write("\n")
      
  fic.close()
# archivoTXT()


def archivoTEXT2():
  listaDeDatos = ['linea1', 'linea2', 'linea3', 'linea4']
  fic = open("text_3.txt", "w")
  fic.writelines("%s\n" % s for s in listaDeDatos)
  fic.close()
# archivoTEXT2()


def lecturaArchivoCSV ():
  # Este es el ejemplo _08semana06clase17EjercicioPandas.py

  # Aqui leemos un archivo .csv
  # y lo cargamos a un dataframe
  
  import pandas as pd
  dataFrame = pd.read_csv('titanic3.csv')
  print (dataFrame)

  # dataFrame.info()
  promedioDeEdades = dataFrame['age'].mean()
  print ('El promedio de edades es: ', promedioDeEdades)
  edadMayor = dataFrame['age'].max()
  edadMenor = dataFrame['age'].min()
  print ('La edad mayor es: ', edadMayor)
  print ('La edad menor es: ', edadMenor)

  promedioTarifa = round ( (dataFrame['fare'].mean()), 2)
  print ('La tarifa promedio es: ', promedioTarifa, 'usd')
  
lecturaArchivoCSV()