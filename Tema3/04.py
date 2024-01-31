import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt

mnist = fetch_openml('mnist_784')
X = mnist.data
y = mnist.target.astype(int)

X_normalized = X / 255.0

num_components = 50

pca = PCA(n_components=num_components)
X_pca = pca.fit_transform(X_normalized)

explained_variance_ratio = pca.explained_variance_ratio_
cumulative_explained_variance = np.cumsum(explained_variance_ratio)

plt.plot(cumulative_explained_variance)
plt.xlabel('Numărul de componente principale')
plt.ylabel('Variația explicată cumulativă')
plt.title('Variația explicată cumulativă prin PCA')
plt.show()

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', alpha=0.7)
plt.colorbar()
plt.xlabel('Componenta Principală 1')
plt.ylabel('Componenta Principală 2')
plt.title('Proiecția datelor MNIST folosind PCA')
plt.show()