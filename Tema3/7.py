import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def get_rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


california_dataset = fetch_california_housing()

df = pd.DataFrame(california_dataset.data, columns=california_dataset.feature_names)
df['MEDV'] = california_dataset.target


X_train, X_predict, y_train, y_predict = train_test_split(california_dataset.data, california_dataset.target,
                                                          test_size=(100-80)/100, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

model_output = model.predict(X_predict)

pe = get_rmse(predictions=model_output, targets=y_predict)
print(f"Prediction error (RMSE): {pe}")

plt.subplot(211)
# show prediction over test data
t = range(1, len(model_output) + 1)
plt.plot(t, y_predict, 'b')
plt.plot(t, model_output, 'g')
plt.legend(['target', 'prediction'])
plt.ylabel("Housing prices")
plt.title("California Dataset median housing value")

plt.subplot(212)
# prediction error
prediction_error = np.sqrt(np.power(model_output - y_predict, 2))
plt.plot(prediction_error, 'b')
plt.legend([f"RMSE: {pe}"])
plt.xlabel("x (samples)")
plt.ylabel("prediction error (RMSE)")
plt.show()


