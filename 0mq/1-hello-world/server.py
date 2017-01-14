import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

nb_request = 0
while True:
    message = socket.recv_string()
    nb_request += 1
    print("received request n°%d: %s" % (nb_request, message))
    socket.send_string("World")
