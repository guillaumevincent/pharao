import time
import zmq
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    area = randrange(25, 200)
    socket.send_string("HOUSE_DATA %i" % area)
    print('send area %sm\u00B2' % area)
    time.sleep(1)
