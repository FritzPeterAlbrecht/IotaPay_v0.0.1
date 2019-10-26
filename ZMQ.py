##> Imports!
import sys
import zmq

ZMQTopic = "tx"  ##> or "tx" or "sn", see https://docs.iota.org/docs/node-software/0.1/iri/references/zmq-events

##> Init ZMQ!
ZMQContext = zmq.Context()
ZMQSocket = ZMQContext.socket(zmq.SUB)
ZMQSocket.connect("tcp://db.iota.partners:5556")
ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, ZMQTopic)

##> Process
while True:

    try:
        update = ZMQSocket.recv(flags=zmq.NOBLOCK).split()
        print(update)
    except:
        pass
