# 12. Utilizați setul de date breast cancer și aplicați K-Means pentru a grupa
# datele, apoi aplicați regresia liniară pentru a prezice variabila țintă 'target',
# iar la final aplicați PCA.

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

breast = load_breast_cancer()
X = breast.data
y = breast.target

#K-Means
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0)
kmeans.fit(X)

# impart setul de date in seturi de antrenament si test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# datele scalate
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# regresie liniara pe datele scalate
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# evaluarea modelului pe setul de test scalat
predictions = model.predict(X_test_scaled)

# aplicarea PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# vizualizarea rez PCA
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel('Componenta principala 1')
plt.ylabel('Componenta principala 2')
plt.title('PCA pentru setul de date Breast Cancer')
plt.show()


