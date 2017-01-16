import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5557")

print("Press Enter when the puller are ready: ")
_ = input()

for i in range(100):
    message = "message n°%d" % i
    print(message)
    socket.send_string(message)

time.sleep(1)