import time
import zmq

context = zmq.Context()

socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5557")

while True:
    print("Received %s" % socket.recv_string())
    time.sleep(0.01)
