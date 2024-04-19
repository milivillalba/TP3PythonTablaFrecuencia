import pandas as pd

#lee los datos quee stan en el archivo AlumnosTabla2.CSV
#carga esos datos en un "DataFrama" llamado "dat_frame"el cual es una extrutura que hace que se vea como una hoja de calculos
data_frame= pd.read_csv("AlumnosTabla2.csv", delimiter=";")

#creo una funcion que toma como entrada los datos(edades y fi) de un archivo "CSV" para relizar los calculos de de la tabla de frecuencia.
def analisis_estadistico(data_frame):
    try:
        
        data_frame["Fi"]= data_frame['fi'].cumsum()#Calculo la frecuencia acumulada'FI',sumando la columna'fi'con"cumsun"
        data_frame["ri"]= data_frame["fi"] / data_frame["fi"].sum()#Calculo la frecuencia relativa'ri' dividiento 'fi' con la suma total de 'fi' que seria la cantidad de alumnos.
        data_frame["Ri"]= data_frame['ri'].cumsum()#Calculo la frecuencia relativa acumulada 'Ri' , acumulando la columna'ri'.
        data_frame['pi%']= data_frame["ri"] * 100 #Calculo el porcentaje de la frecuencia relativa'pi%' multiplicando 'ri' por 100.
        data_frame['Pi%']= data_frame['Ri'] * 100 #Calculo el porcentaje de la frecuencia relativa acumulada'Pi%' multiplicando 'Ri' por 100.

        print(data_frame)
        
    except ValueError:
        #Si hay un error al obtener los datos del archivo se muestra este mensaje.
        print("Error en obtener los datos de la listalista")
        


analisis_estadistico(data_frame)
data_frame.to_clipboard(index=False, decimal=',')