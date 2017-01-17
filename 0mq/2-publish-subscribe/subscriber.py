import json

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print('Collecting house data…')
socket.connect('tcp://127.0.0.1:5556')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    house = socket.recv_json()
    print('message received: %s' % json.dumps(house))
