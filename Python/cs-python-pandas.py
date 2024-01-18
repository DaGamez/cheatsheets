# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:25:41 2023

@author: dagam
"""

import pandas as pd




#se crea serie con indices default 0,1,2
b = [1, 7, 2]
myvarB = pd.Series(b)
print(myvarB[1])

#se crea serie con indices especificados
myvarB2 = pd.Series(b, index = ["x", "y", "z"])
print(myvarB2["y"])
print(myvarB2[1])

#creating a series with a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
myvarC = pd.Series(calories)


#data frame
mydatasetA = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvarA = pd.DataFrame(mydatasetA)

#locate row, returns a pandas Series
print(myvarA.loc[0])

#to create with index
myvarA2 = pd.DataFrame(mydatasetA, index=["day1", "day2", "day3"])
print(myvarA2.loc["day2"])

#mirar cabeza
myvarA2.head(1)


#mirar la cola
myvarA2.tail(1)

#mirar info
myvarA2.info()


#leer de un csv
df = pd.read_csv('data.csv') 

#leerde un json
df = pd.read_json('data.json')

#borrar filas con celdas en na
new_df = df.dropna()

#reemplazar nas, inplace sirve para cambiar df original
df.fillna(130, inplace = True) 

#reemplazar solo para una columna
df["Calories"].fillna(130, inplace = True)

#convertir a fecha
df['Date'] = pd.to_datetime(df['Date'])

#borrar filas con duracion de mas 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

df.duplicated() #devuelve true por cada fila q es un duplicado

#quitar duplicados
df.drop_duplicates(inplace = True)

#correlacion
df.corr()



#graficas
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df.plot()
plt.show()

#dataframe with multi index
df = pd.DataFrame(
{"a" : [4 ,5, 6], 
"b" : [7, 8, 9], 
"c" : [10, 11, 12]}, 
index = pd.MultiIndex.from_tuples([("d", 1), ("d", 2),("e", 2)], names=["n", "v"]))



