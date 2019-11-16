#import sys
import zmq


class ZMQ:
    def __init__(self, state):
        # > Init ZMQ!
        self.ZMQContext = zmq.Context()
        self.ZMQSocket = self.ZMQContext.socket(zmq.SUB)
        self.ZMQSocket.connect("tcp://zmq.devnet.iota.org:5556")
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, "tx")
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, "sn")

        self.state = state

    def listen(self):
        # > Process

        try:
            zmq_response = self.ZMQSocket.recv(flags=zmq.NOBLOCK).decode().split()
            event = str(zmq_response[0])
            address = str(zmq_response[2])
            value = int(zmq_response[3])
            # catch tx for actual address
            if event == "tx":
                if address == self.state.last_used_address[0:81]:
                    self.state.tx_hash = zmq_response[1]
                    if value != 0:
                        self.state.user_credit = value
                        self.state.set(1)
                        print("Value TX incoming: " + str(value) + " iota")
                    else:
                        self.state.set(7)

        except:
            pass

    def check_confirmation(self):
        # > Process

        try:
            zmq_response = self.ZMQSocket.recv(flags=zmq.NOBLOCK).decode().split()
            event = str(zmq_response[0])

            # catch confirmation message for actual address
            if event == "sn":
                conf_hash = zmq_response[2]
                if conf_hash == self.state.tx_hash:
                    self.state.set(2)
                    print("CONFIRMED")

        except:
            pass
