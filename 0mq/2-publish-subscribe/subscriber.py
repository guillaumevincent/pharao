import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print('Collecting house data…')
socket.connect('tcp://localhost:5556')
socket.setsockopt_string(zmq.SUBSCRIBE, 'HOUSE_DATA')
message_received = socket.recv_string()
print('message: %s' % message_received)
print("area: %s" % message_received.split(' ')[1])
