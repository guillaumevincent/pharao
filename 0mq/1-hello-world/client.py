import sys

import time
import zmq

context = zmq.Context()

print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

client_name = 'client_' + sys.argv[1]
tempo = int(sys.argv[2])

for request in range(100):
    time.sleep(tempo / 1000)
    print("Sending request n° %s" % request)
    socket.send_string("%s: Hello" % client_name)

    reply = socket.recv_string()
    print("Received reply %s [ %s ]" % (request, reply))
