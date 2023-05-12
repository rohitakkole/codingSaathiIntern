import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

iris = pd.read_csv(r"Iris.csv")
print(iris.head())

print(iris.describe())

print("Target Labels", iris["Species"].unique())

   
fig = px.scatter(iris, x="SepalWidthCm", y="SepalLengthCm", color="Species")
fig.show()

x = iris.drop("Species", axis=1)
y = iris["Species"]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                    test_size=0.2, 
                                                    random_state=0)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train.values, y_train)

x_new = np.array([[6, 2.2, 1, 0.2,6]])
prediction = knn.predict(x_new)
print("Prediction: {}".format(prediction))
