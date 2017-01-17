import csv

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print('subscribe to awesome houses data…')
socket.connect('tcp://127.0.0.1:5558')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    house = socket.recv_json()
    print(house)
    with open('houses.csv', 'a') as csvfile:
        fieldnames = ['id', 'surface', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(house)
