import pandas as pd

#lee los datos quee stan en el archivo AlumnosTabla2.CSV

#creo una funcion que toma como entrada los una lista de edades.
def analisis_estadistico(data):
   
        #creo un data_frame a partir de valores
        data_Serie= pd.Series(data) # '.series' es una extrutura de datos unidimencional que contiene datos etiquetados
        
        fi= data_Serie.value_counts().sort_index() #cuento la frecuencia de cada valor unico en la lista y devuelve una nueva serie donde los indices son valores unicos.
        Fi= fi.cumsum()#Calculo la frecuencia acumulada'FI',sumando la columna'fi'con"cumsun"
        ri= fi / fi.sum()#Calculo la frecuencia relativa'ri' dividiento 'fi' con la suma total de 'fi' que seria la cantidad de alumnos.
        Ri= ri.cumsum()#Calculo la frecuencia relativa acumulada 'Ri' , acumulando la columna'ri'.
        pi= ri* 100 #Calculo el porcentaje de la frecuencia relativa'pi%' multiplicando 'ri' por 100.
        Pi= Ri * 100 #Calculo el porcentaje de la frecuencia relativa acumulada'Pi%' multiplicando 'Ri' por 100.

       #creo una dataFrama para acomodar y mostra los datos d ela tabla de frecuencia
        tablaFrecuencia= pd.DataFrame({
           'Edades': fi.index, #agrego una columna con las edades
           'fi': fi,
           'Fi': Fi,
           'ri':ri,
           'Ri': Ri,
           'pi%': pi,
           'Pi%': Pi
         
       })
        return tablaFrecuencia
        
    

# Lista de datos de prueba
lista_Edades= [18, 19, 19, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 25, 25, 28, 28, 29, 30, 30, 35, 38]

# Llamar a la función para analizar los datos y mostrar la tabla de frecuencia
resultado_tabla = analisis_estadistico(lista_Edades)
print(resultado_tabla)

#Convertir con archivo 'CSV'
resultado_tabla.to_csv('TablaEdades.csv', index=False)