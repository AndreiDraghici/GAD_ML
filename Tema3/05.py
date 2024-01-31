import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

olivetti_faces = datasets.fetch_olivetti_faces()
images = olivetti_faces.images
labels = olivetti_faces.target

n_samples, h, w = images.shape
X = images.reshape((n_samples, h * w))

n_components = 150
pca = PCA(n_components=n_components, svd_solver='randomized', whiten=True).fit(X)

X_pca = pca.transform(X)

images_reconstructed = pca.inverse_transform(X_pca)
images_reconstructed = images_reconstructed.reshape((n_samples, h, w))

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(images[0], cmap=plt.cm.gray)
plt.title('Imagine originală')
plt.subplot(1, 2, 2)
plt.imshow(images_reconstructed[0], cmap=plt.cm.gray)
plt.title('Imagine reconstruită')
plt.show()

eigenfaces = pca.components_.reshape((n_components, h, w))
plt.figure(figsize=(10, 20))
for i in range(10):
    plt.subplot(5, 2, i + 1)
    plt.imshow(eigenfaces[i], cmap=plt.cm.gray)
    plt.title(f'Componenta principală {i+1}')
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Numărul de componente')
plt.ylabel('Variație explicată cumulativă')
plt.show()