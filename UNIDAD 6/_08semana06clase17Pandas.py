# Lunes 7 de Junio

# Pandas + ejercicio practico

# https://devopedia.org/images/article/60/7938.1587985662.jpg

# https://storage.googleapis.com/lds-media/images/series-and-dataframe.width-1200.png

# clase del dia lunes 7 de junio
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas.core.series import Series

# Esta serie pertenece a la población en Millones de determinados paises
serie = pd.Series ([51,32,45,0.5,6.5,19.5,9.5,17,7,3.5,11.5,28.5,126,212,0.4])
print (serie)

# Asignamos a los indices los nombres correspondientes
serie.index = ['Colombia', 'Perú', 'Argentina', 'Surinam', 'Nicaragua', 'Chile', 
              'Honduras', 'Guatemala', 'Paraguay', 'Uruguay', 'Bolivia', 
              'Venezuela', 'México', 'Brasil', 'Belize']
serie.name = 'Poblacion'
print (serie)

# Imprimir solo la población de Colombia
print ('Población de Colombia: ', serie['Colombia']) # Observe el indice

# Imprimir solo la población de Argentina
print ('Población de Argentina: ', serie.Argentina) # Observe el indice

# Imprimir la población de paises en especifico
print ('Poblacion de algunos paises en especifico: ')
print (serie [['Argentina', 'Colombia']] ) # Observe los indices


print ('media ', serie.mean())
print ('mediana ', serie.median())
print ('desv estándar ', serie.std())
print ('maximo ', serie.max())
print ('minimo ', serie.min())

print ('Describe: ')
print (serie.describe())

# figura, ejes = plt.subplots (1, 4, figsize = (12,3))
# serie.plot (ax = ejes[0], kind = 'line', title = 'line')
# serie.plot (ax = ejes[1], kind = 'bar', title = 'bar')
# serie.plot (ax = ejes[2], kind = 'box', title = 'box')
# serie.plot (ax = ejes[3], kind = 'pie', title = 'pie')

dataFrame = pd.DataFrame ( {'Población': [51,32,45,0.5,6.5,19.5,9.5,17,7,3.5,11.5,
                             28.5,126,212, 0.4],
                           'Idioma':['Español', 'Español','Español','Neerlandés',
                                     'Español','Español','Español','Español',
                                     'Español','Español','Español','Español',
                                     'Español','Portugués','Inglés']
                           },
                           index = ['Colombia', 'Perú', 'Argentina', 'Surinam', 'Nicaragua', 'Chile', 
                                    'Honduras', 'Guatemala', 'Paraguay', 'Uruguay', 'Bolivia', 
                                    'Venezuela', 'México', 'Brasil', 'Belize']
                          )
print ('DataFrame a partir de una estructura tipo dict')
print (dataFrame)

poblaciones = dataFrame ['Población']
print ('Columna población: ')
print (poblaciones)


datosDeMexico = dataFrame.loc['México']
print ('Los datos de mexico son: ')
print (datosDeMexico)
# Población      126.0
# Idioma       Español

poblacionDeMexYCol  =  dataFrame.loc[['México', 'Colombia'],'Población']
print ('La población de México y Colombia es: ')
print (poblacionDeMexYCol)
# La población de México y Colombia es:
# México      126.0
# Colombia     51.0
# Name: Población, dtype: float64


# Enlace con el ejercicio completo
# https://replit.com/join/iudcqzlr-pyplusplusmf