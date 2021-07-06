def funcionReto5 (nombreDelArchivo: str) -> dict:
    import pandas as pd
    dataFrame = pd.read_csv(nombreDelArchivo)
    # print (dataFrame)
    
    # dataFrame.info()
    promedioDeEdades = dataFrame['age'].mean()
    edadMayor = dataFrame['age'].max()
    edadMenor = dataFrame['age'].min()
    promedioTarifa = round ( (dataFrame['fare'].mean()), 2)

    # El diccionario de salida, se puede armar al final
    # o al principio
    diccionarioSalida = dict()
    diccionarioSalida ['promedioEdades'] = promedioDeEdades
    diccionarioSalida ['edadMayor'] = edadMayor 
    diccionarioSalida ['edadMenor'] = edadMenor
    diccionarioSalida ['promedioTarifa'] = promedioTarifa

    return diccionarioSalida


print (funcionReto5('titanic3.csv'))

# {'promedioEdades': 29.8811345124283, 'edadMayor': 80.0, 'edadMenor': 0.1667, 'promedioTarifa': 33.3}ejemplo de dataframes 
# _08semana06clase17EjercicioPandas.py

