import pandas as pd

data = {'Nume':['Ana','Bogdan', 'Cristina'],
        'Varsta':[25, 30, 22],
        'Salariu':[50000,60000,45000]}


df = pd.DataFrame(data)
#print(df)

#nume = df['Nume']
#print(nume)

#index pt persoana si eticheta pt print
#salariu_Bogdan = df.at[1,'Salariu']
#print(salariu_Bogdan)

#adaugare coloana noua
df['Experienta'] = [2,5,1]
#print(df)

# df.set_index(keys='Nume',inplace=True)
# #print(df.loc['Bogdan'])
# #print(df.iloc[1])
# #print(df.loc[['Ana', 'Cristina'],['Varsta','Salariu']])
# df_filtrat = df[df['Varsta']>25]
# print(df_filtrat)
# df_complex =df[(df['Varsta']>=22) & (df['Experienta'] >=2)]
# print(df_complex)



# df_sortat = df.sort_values(by='Varsta', ascending=False)
# print(df_sortat)



#
# data = {'Nume': ['Ana', 'Bogdan', 'Ana', 'Cristina', 'David', 'Ana'],
#         'Varsta':[25,30,25,22,35,25],
#         'Salariu':[50000,60000,50000,45000,70000,50000]
#         }
#
# df = pd.DataFrame(data)
# print(df)
#
# print('=============')

# df_fara_duplicate = df.drop_duplicates()
# print(df_fara_duplicate)

#
# data = {'Nume': ['Ana', 'Bogdan', None, 'Cristina', 'David'],
#         'Varta':[25,30,None,22,35],
#         'Salariu':[50000, None, 45000, 70000, 60000]}
#
# df = pd.DataFrame(data)
# print(df)
#
#
# print('========')
#
# df_fara_randuri = df.dropna()
# print(df_fara_randuri)
#
# print('=============')
# df_cu_zero = df.fillna(0)
# print(df_cu_zero)
#

#
# data = {'Nume': ['Ana', 'Bogdan', 'Cristina', 'David', 'Elena', 'Florin'],
#         'Varsta':[25,30,22,35, 28, 40],
#         'Salariu':[50000, 60000, 45000, 70000, 55000, 80000],
#         'Departamente':['IT', 'HR', 'IT', 'HR','IT', 'HR']}
#
# df = pd.DataFrame(data)
# print(df)
# print("===========")
# grupuri_departament = df.groupby('Departamente')
# # for nume_departament, grup in grupuri_departament:
# #     print(grup)
# #     print("")
#
# # medie_salarii = grupuri_departament['Salariu'].mean()
# # print(medie_salarii)
# #
#
# rezultate_agregare = grupuri_departament.agg({'Varsta': 'mean', 'Salariu': ['sum','median'],'Nume':'count'})
# print(rezultate_agregare)


# data = {'Data':['2022-01-01','2022-02-01','2022-03-01'],
#         'Vanzari':[100, 150,200]}
#
# df = pd.DataFrame(data)
# print(df)
# df['Data'] = pd.to_datetime(df['Data'])
# print(df)
# df['Zi'] = df['Data'].dt.day
# print(df)
#
# df['Luna']= df['Data'].dt.month
# df['An'] = df['Data'].dt.year
# print(df)
#
# df['Diferenta_zi'] = (df['Data'] - pd.to_datetime('2022-01-01')).dt.days
# print(df)

df1 = pd.DataFrame({'ID':[1,2,3],
                    'Nume':['Ana', 'Bogdan','Silviu'],
                    'Varsta':[25,30,34]}, index=[1,2,3])

df2 = pd.DataFrame({'ID':[2,3,4],
                    'Nume':['Cristina','David','Maria'],
                    'Varsta':[22,35,21]}, index=[2,3,4])

# df_concat_randuri = pd.concat([df1,df2],ignore_index=True)
# print(df_concat_randuri)

# df_concat_coloane = pd.concat(objs=[df1,df2],axis=1)
# print(df_concat_coloane)

# df_merge = pd.merge(df1,df2,on="ID", how='outer')
#print(df_merge)
#
# df_join = df1.join(df2, how='inner')
# print(df_join)



data = {'Nume': ['Ana', 'Bogdan', 'Cristina', 'David', 'Elena', 'Florin'],
        'Varsta':[25,30,22,35, 28, 40],
        'Salariu':[50000, 60000, 45000, 70000, 55000, 80000],
        'Departamente':['IT', 'HR', 'IT', 'HR','IT', 'HR']}

# df = pd.DataFrame(data)
# df.to_csv('date.csv',index=False)

df = pd.read_csv('date.csv')
print(df)