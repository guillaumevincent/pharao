import json

import numpy as np
import zmq
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

x = []
y = []
for house in classified_houses:
    if house['label'] == 1:
        x.append([house['price']])
        y.append(house['surface'])

x_train_data = x[0:-50]
x_test_data = x[-50:]
y_train_data = y[:-50]
y_test_data = y[-50:]

regr = linear_model.LinearRegression()
regr.fit(x_train_data, y_train_data)

context = zmq.Context()

leboncoin_socket = context.socket(zmq.PULL)
leboncoin_socket.connect("tcp://127.0.0.1:5557")

awesome_house_socket = context.socket(zmq.PUB)
awesome_house_socket.bind("tcp://127.0.0.1:5558")

print('waiting houses on port 5557...')
print('publish awesome houses on port 5558...')

while True:
    house = leboncoin_socket.recv_json()
    prediction_area = regr.predict(house['price'])
    if np.math.sqrt((prediction_area - 90) ** 2) < prediction_area * 0.1:
        print('awesome house %s€ for %sm\u00B2' % (house['price'], house['surface']))
        awesome_house_socket.send_json(house)
    else:
        print('rejected house %s€ for %sm\u00B2' % (house['price'], house['surface']))
