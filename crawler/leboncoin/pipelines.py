import json

import zmq


class ZMQPipeline(object):
    def open_spider(self, spider):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        self.socket.bind("tcp://127.0.0.1:5557")

    def close_spider(self, spider):
        self.socket.close()
        self.context.term()

    def process_item(self, item, spider):
        self.socket.send_string(json.dumps(dict(item)))
        return item
