import pandas as pd

data_frame= pd.read_csv("pruebaPythonCsv.csv")

data_frame["Fi"]= data_frame['fi'].cumsum()#acumula
data_frame["fr"]= data_frame["fi"] / data_frame["fi"].sum()
data_frame["Fr"]= data_frame['fr'].cumsum()
data_frame['pi%']= data_frame["fr"] * 100
data_frame['Pi%']= data_frame['Fr'] * 100

print(data_frame) #con los corchete acsede a las columnas en concreto

#para copiar la tabla de frecuencia 

data_frame.to_clipboard(index=False , decimal=',')
