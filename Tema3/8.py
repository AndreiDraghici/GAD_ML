#8. Utilizați setul de date iris și aplicați algoritmul K-Means pentru a grupa
# datele în 3 clustere, bazându-vă pe caracteristicile 'sepal length' și 'sepal
# width'.

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data[:, :2]  # caracteristicile 'sepal length' si 'sepal width'

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

labels = kmeans.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('algoritmul K-Means pe setul Iris')
plt.show()







