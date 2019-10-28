##> Imports!
import sys
import zmq


class ZMQ:

    def __init__(self, last):
    ##> Init ZMQ!
        self.last = last
        self.ZMQTopic = "tx" ##> or "tx" or "sn", see https://docs.iota.org/docs/node-software/0.1/iri/references/zmq-events
        self.ZMQContext = zmq.Context()
        self.ZMQSocket = self.ZMQContext.socket(zmq.SUB)
        self.ZMQSocket.connect("tcp://db.iota.partners:5556")
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, self.ZMQTopic)

    def listen(self):
        ##> Process
        while True:

            try:
                listen = self.ZMQSocket.recv(flags=zmq.NOBLOCK).split()
                address = str(listen[2])
                self.address = address[2:83] ##> es gibt sicher einen besseren weg ein bytestring in einen string umzuwandeln
                self.last = self.last[0:81]
                if self.address == self.last:
                    self.value = str(listen[3]) ##>> das sollte besser ein integer sein

                    print('New TX incoming', self.value) ##> self.value kommt im falschen format (b'0') bytestring>string
                    break ##> nur weil die folgende if abfrage nicht funktioniert wegen formatfehler
                    if self.value == 0:
                        print('Zero Value TX received - try again')
                        break
                    if self.value >= 0:
                        print('Thank you for the tx of ', self.value)
                        return self.value

                print(self.address)

            except:
                pass
