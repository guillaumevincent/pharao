import json
import time
from random import randrange

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5556")

while True:
    house = {'area': randrange(25, 200)}
    socket.send_json(house)
    print('send house: %s' % json.dumps(house))
    time.sleep(5)
