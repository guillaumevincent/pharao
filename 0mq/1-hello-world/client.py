import zmq

context = zmq.Context()

print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    reply = socket.recv()
    print("Received reply %s [ %s ]" % (request, reply))
