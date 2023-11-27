import datetime

import pandas as pd
import numpy as np

#serie din lista
#lista =[10, 20, 30, 40, 50]

#serie = pd.Series(lista)

#print(serie)

# din array numpy
# array_date = np.array([10, 20, 30, 40, 50])
#
# serie = pd.Series(array_date)
# print (serie)

#din dinctionar
# dict_date = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
# serie = pd.Series(dict_date)
# print (serie)



# putem introduce etichte
# date = [10, 20, 30, 40, 50]
# etichete = ['a','b','c','d','e']
#
# serie = pd.Series(date, index=etichete)
# print(serie)




ser = pd.Series(data=[10, 20, 30, 40, 50], index =['a','b','c','d','e'])
# print(ser['b'])
# print(ser[['a','c','e']])
# #cand facem slice in etichete, python ia si ultima eticheta, la index NU
# print(ser['b':'d'])
#print(ser[1:4])
#print cu conditie
#print(ser[ser>20])


date_si_timp = [datetime.datetime(2022,1,1),
                datetime.datetime(2022,1,2),
                datetime.datetime(2022,1,3)]
ser_temp = pd.Series(data=[10,20,30],index=date_si_timp)
#print(ser_temp['2022-01-02'])
print(ser_temp['2022-01-01':'2022-01-02'])

