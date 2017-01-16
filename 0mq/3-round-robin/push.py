import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5557")

for i in range(10000):
    message = "message n°%d" % i
    print(message)
    socket.send_string(message)
