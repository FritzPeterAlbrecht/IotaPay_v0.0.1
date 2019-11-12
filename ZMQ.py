import sys
import zmq


class ZMQ:

    def __init__(self, last):
        # > Init ZMQ!
        self.last = last
        #self.ZMQTopic = "tx"  # > or "tx" or "sn", see https://docs.iota.org/docs/node-software/0.1/iri/references/zmq-events
        self.ZMQContext = zmq.Context()
        self.ZMQSocket = self.ZMQContext.socket(zmq.SUB)
        self.ZMQSocket.connect("tcp://zmq.devnet.iota.org:5556")
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, 'tx')
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, 'sn')
        self.info = str(self.last[0:41] + '\n' + self.last[
                        42:81] + '\n' + 'CHECKSUM: ' + self.last[82:91])
        self.value = 0

    def listen(self):
        # > Process
        while True:

            try:
                zmq_response = self.ZMQSocket.recv(flags=zmq.NOBLOCK).decode().split()
                print(zmq_response)
                address = str(zmq_response[2])
                value = int(zmq_response[3])
                self.address = address
                self.last = self.last[0:81]
                if self.address == self.last:
                    self.value = value
                    if self.value != 0:
                        self.info = str('Thank you for the tx of ' + str(self.value) + ' iota')
                        return self.value

                    else:
                        self.info = 'ERROR: Zero Value TX received - try again!'
                        print('Zero Value TX')
                        break

            except:
                pass
