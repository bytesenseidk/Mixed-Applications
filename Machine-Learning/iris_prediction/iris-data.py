import os
import sklearn
import numpy as np
import pandas as pd
from sklearn import linear_model, preprocessing, datasets
from sklearn.neighbors import KNeighborsClassifier

# Load data set
data = pd.read_csv("iris.csv", sep=";")

# Preprocess / Clean data
proc = preprocessing.LabelEncoder()
sepal_length = proc.fit_transform(list(data["sepal_length"]))
sepal_width = proc.fit_transform(list(data["sepal_width"]))
petal_length = proc.fit_transform(list(data["petal_length"]))
petal_width = proc.fit_transform(list(data["petal_width"]))
species = proc.fit_transform(list(data["species"]))

# Prediction
predict = "species"

x = list(zip(sepal_length, sepal_width, petal_length, petal_width))
y = list(species)

# Train and predict
vari = ["Setosa", "Virginica", "Versicolor"]
best = 0
worst = 100
for i in range(100):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.9)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    if accuracy > best:
        best = accuracy

    elif accuracy < worst:
        worst = accuracy

    prediction = model.predict(x_test)

    print(f"Prediction:\t{vari[prediction[i]].ljust(10)}\tActual: {vari[y_test[i]].ljust(10)}\t\
                        Accuracy: {str(round(accuracy * 100, 2)).ljust(5)}%\tData: {x_test[i]}")

print(f"\nHighest Accuracy: {round((best * 100), 2)}%")
print(f"Worst Accuracy: {round((worst * 100), 2)}%")

