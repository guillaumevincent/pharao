var zmq = require('zmq');

var sock = zmq.socket('pull');
sock.connect('tcp://127.0.0.1:5557');

sock.on('message', function (msg) {
    console.log('Received %s', msg.toString());
});