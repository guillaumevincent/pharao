import json

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

classified_houses = []
with open('houses.json') as data_file:
    houses = json.load(data_file)
    houses = houses[:len(houses) - len(houses) % 2]
    for house in houses:
        h = {'surface': house['surface'], 'price': house['price'], 'label': 1}
        square_price = int(house['price']) / int(house['surface'])
        if square_price < 1000 or square_price > 5000 or house['surface'] > 300 or house['surface'] < 25:
            h['label'] = 0
        classified_houses.append(h)

x_all = [h['price'] for h in classified_houses]
y_all = [h['surface'] for h in classified_houses]

x_good = []
y_good = []
x = []
y = []
for house in classified_houses:
    if house['label'] == 1:
        x.append([house['price']])
        x_good.append(house['price'])
        y.append(house['surface'])
        y_good.append(house['surface'])

x_train_data = x[0:-50]
x_test_data = x[-50:]
y_train_data = y[:-50]
y_test_data = y[-50:]

regr = linear_model.LinearRegression()
regr.fit(x_train_data, y_train_data)

plt.plot(x_all, y_all, 'bo')
plt.plot(x_good, y_good, 'ro')
plt.scatter(x_test_data, y_test_data, color='red')
plt.plot(x_test_data, regr.predict(x_test_data), color='black', linewidth=3)
plt.axis([0, 1200000, 0, 1000])

print(regr.predict(170000))
print('Coefficients: \n', regr.coef_)
print("Mean squared error: %.2f" % np.mean((regr.predict(x_test_data) - y_test_data) ** 2))
print('Variance score: %.2f' % regr.score(x_test_data, y_test_data))
plt.ylabel('area square meter')
plt.xlabel('price')
plt.title('linear regression Bordeaux houses')
plt.show()
