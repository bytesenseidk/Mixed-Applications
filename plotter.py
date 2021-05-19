import sklearn
import numpy as pd
import pandas as pd
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("iris.csv", sep=";")
# data = data[["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]]
# predict = "species"

print(data.columns)


# X = np.array(data.drop([predict], 1))
# y = np.array(data[predict])

# x_train, y_train, x_test, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

# linear = linear_model.LinearRegression()
# linear.fit(x_train, y_train)
# accuracy = linear.score(x_test, y_test)
# print(accuracy)

# predictions = linear.predict(x_test)
# for x in range(len(predictions)):
#      print(predictions[x], x_test[x], y_test[x])