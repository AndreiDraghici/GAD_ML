import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load wine dataset
wine = load_wine()
data = pd.DataFrame(data=wine.data, columns=wine.feature_names)
data['target'] = wine.target

# extract features and target
X = data.drop('target', axis=1)
y = data['target']

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply DBSCAN to group data
dbscan = DBSCAN(eps=2, min_samples=5)
clusters = dbscan.fit_predict(X_scaled)

# Add cluster to data
data['cluster'] = clusters

print(data)
print(data['cluster'].unique())

# Train the Linear Regression
X_train, X_test, y_train, y_test = train_test_split(data.drop('target', axis=1), y, test_size=0.2, random_state=42)
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

# Predict
y_pred = linear_regression.predict(X_test)

# Evaluate performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)
