# 9. Utilizați setul de date digits și aplicați PCA pentru a reduce
# dimensionalitatea datelor și pentru a vizualiza varianța explicată de diferite
# număr de componente principale.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# setul de date digits
digits = load_digits()
X = digits.data
y = digits.target

# scalarea datelor
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

varianță_acumulată = np.cumsum(pca.explained_variance_ratio_)

# vizualizarea variantei explicata
plt.figure(figsize=(8, 4))
plt.plot(varianță_acumulată, marker='o')
plt.xlabel('Numarul de componente')
plt.ylabel('Varianta acumulata')
plt.title('Varianta explicata de diferite numar de componente principale')
plt.grid(True)
plt.show()


