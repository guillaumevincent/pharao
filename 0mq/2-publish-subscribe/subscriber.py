import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print('Collecting house data…')
socket.connect('tcp://127.0.0.1:5556')
socket.setsockopt_string(zmq.SUBSCRIBE, 'HOUSE_DATA')

while True:
    message_received = socket.recv_string()
    print('message: %s' % message_received)
    print("area: %sm\u00B2" % message_received.split(' ')[1])
