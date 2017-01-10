from sklearn import tree

import json

training_target = []
training_data = []

test_data = []
test_target = []
with open('houses.normalized.json') as data_file:
    houses = json.load(data_file)
    houses = houses[:len(houses) - len(houses) % 2]
    for i, house in enumerate(houses):
        if i % 2 == 0:
            training_data.append([house['price'], house['surface']])
            training_target.append(house['label'])
        else:
            test_data.append([house['price'], house['surface']])
            test_target.append(house['label'])

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(training_data, training_target)

print(len(test_target))
print(len(test_data))
print(len(training_data))
print(len(training_target))
print(test_target[0], test_target[10])
predictions = classifier.predict(test_data)
print(predictions[0], predictions[10])




import matplotlib.pyplot as plt
plt.plot(test_data[:, 0],test_data[:, 1])
plt.ylabel('some numbers')
plt.show()