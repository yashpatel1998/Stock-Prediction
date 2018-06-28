# -*- coding: utf-8 -*-
import csv
import time
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from numba import jit

X = []
y = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader) # skipping column names
        for row in csvFileReader:
            date_str = str(row[0])
            pattern = '%Y-%m-%d'
            epoch = int(time.mktime(time.strptime(date_str, pattern)))
            X.append(epoch)
            y.append(float(row[4]))

    return


get_data('SENSEX2.csv')
X = np.reshape(X, (len(X), 1)) # converting to matrix of n X 1
y = np.reshape(y, (len(y), 1))

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/6, random_state = 0)

# Fitting in the regressor
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)

score = regressor.score(X_test,y_test)

y_pred_rand = regressor.predict(1530057600000)
# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Date vs Price (Training set)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()