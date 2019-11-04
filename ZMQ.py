import sys
import zmq


class ZMQ:

    def __init__(self, last):
        # > Init ZMQ!
        self.last = last
        self.ZMQTopic = "tx"  # > or "tx" or "sn", see https://docs.iota.org/docs/node-software/0.1/iri/references/zmq-events
        self.ZMQContext = zmq.Context()
        self.ZMQSocket = self.ZMQContext.socket(zmq.SUB)
        self.ZMQSocket.connect("tcp://db.iota.partners:5556")
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, self.ZMQTopic)
        self.info = str(self.last[0:41] + '\n' + self.last[
                        42:81] + '\n' + 'CHECKSUM: ' + self.last[82:91])
        self.value = int()

    def listen(self):
        # > Process
        while True:

            try:
                zmq_response = self.ZMQSocket.recv(flags=zmq.NOBLOCK).split()
                address = str(zmq_response[2])
                self.address = address[2:83]  # > es gibt sicher einen besseren weg
                self.last = self.last[0:81]
                if self.address == self.last:
                    self.value = int(zmq_response[3])
                    self.info = 'New TX incoming, waiting for confirmation'

                    if self.value == 0:
                        print('Zero Value TX received - try again')
                        break
                    if self.value >= 0:
                        print('Thank you for the tx of ', self.value, 'iota')
                        return self.value

            except:
                pass
