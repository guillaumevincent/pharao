import json
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

training_houses = []
with open('houses.json') as data_file:
    houses = json.load(data_file)
    houses = houses[:len(houses) - len(houses) % 2]
    for house in houses:
        training_house = {'surface': house['surface'], 'price': house['price'], 'label': 1}
        square_price = int(house['price']) / int(house['surface'])
        if square_price < 1000 or square_price > 5000 or house['surface'] > 300 or house['surface'] < 25:
            training_house['label'] = 0
        training_houses.append(training_house)

X = []
Y = []
X2 = []
Y2 = []
x_all = []
y_all = []
for i, house in enumerate(training_houses):
    if house['label'] == 1:
        x_all.append([house['price']])
        y_all.append(house['surface'])
        X.append(house['price'])
        Y.append(house['surface'])
    else:
        X2.append(house['price'])
        Y2.append(house['surface'])

x_train_data = x_all[:-50]
x_test_data = x_all[-50:]
y_train_data = y_all[:-50]
y_test_data = y_all[-50:]
regr = linear_model.LinearRegression()
regr.fit(x_train_data, y_train_data)
print('Coefficients: \n', regr.coef_)
print("Mean squared error: %.2f" % np.mean((regr.predict(x_test_data) - y_test_data) ** 2))
print('Variance score: %.2f' % regr.score(x_test_data, y_test_data))
plt.scatter(x_train_data, y_train_data, color='black')
plt.plot(X, Y, 'ro')
plt.plot(x_train_data, regr.predict(x_train_data), color='green', linewidth=1)
plt.plot(X2, Y2, 'bo')
plt.axis([0, 1200000, 0, 1000])
plt.plot([0, 1000*1000], [0, 1000], 'r--')
plt.plot([0, 240*5000], [0, 240], 'r--')
plt.ylabel('area square meter')
plt.xlabel('price')
plt.title('linear regression Bordeaux houses')
plt.show()
