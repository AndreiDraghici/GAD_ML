import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns

# Load the digits dataset
digits = load_digits()
data, target = digits.data, digits.target

# Use K-Means
kmeans = KMeans(n_clusters=10, random_state=42, n_init=10)
clusters = kmeans.fit_predict(data)

# Use PCA on the clusters
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data)

# Create a new dataframe for results
result_df = pd.DataFrame({'PC1': reduced_data[:, 0], 'PC2': reduced_data[:, 1], 'Cluster': clusters, 'Target': target})
print(result_df)

# Show the 2D data
plt.figure(figsize=(12, 8))
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=result_df, palette='Dark2')
plt.title('K-Means and PCA on the digits dataset')
plt.show()

