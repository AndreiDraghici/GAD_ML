import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data"
data = pd.read_csv(url, header=None)
data.columns = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']

features = data[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]

pca = PCA(n_components=2)  # Reducem la 2 componente principale pentru vizualizare
principalComponents = pca.fit_transform(features)

principalDf = pd.DataFrame(data=principalComponents, columns=['Principal Component 1', 'Principal Component 2'])

finalDf = pd.concat([principalDf, data[['Type']]], axis=1)


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 Component PCA', fontsize=20)

types = [1, 2, 3, 4, 5, 6, 7]
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for type, color in zip(types, colors):
    indicesToKeep = finalDf['Type'] == type
    ax.scatter(finalDf.loc[indicesToKeep, 'Principal Component 1'], finalDf.loc[indicesToKeep, 'Principal Component 2'], c=color, s=50)
ax.legend(types)
ax.grid()
plt.show()
data.head(100).to_csv('Glass.csv', index=False)