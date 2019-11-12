import sys
import zmq


class ZMQ:
    def __init__(self, last_used_address, state):
        # > Init ZMQ!
        self.last_used_address = last_used_address
        # self.ZMQTopic = "tx"  # > or "tx" or "sn", see https://docs.iota.org/docs/node-software/0.1/iri/references/zmq-events
        self.ZMQContext = zmq.Context()
        self.ZMQSocket = self.ZMQContext.socket(zmq.SUB)
        self.ZMQSocket.connect("tcp://zmq.devnet.iota.org:5556")
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, "tx")
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, "sn")
        self.info = str(
            self.last_used_address[0:41]
            + "\n"
            + self.last_used_address[42:81]
            + "\n"
            + "CHECKSUM: "
            + self.last_used_address[82:91]
        )
        self.value = 0
        self.state = state

    def listen(self):
        # > Process

        try:
            zmq_response = self.ZMQSocket.recv(flags=zmq.NOBLOCK).decode().split()
            # print(zmq_response)
            # print("received trytes")
            address = str(zmq_response[2])
            value = int(zmq_response[3])

            self.last_used_address = self.last_used_address[0:81]
            if address == self.last_used_address:
                self.value = value
                if self.value != 0:
                    self.state.set_state(
                        1, "Thank you for the tx of " + str(self.value) + " iota"
                    )

                else:
                    self.state.set_state(
                        -1, "ERROR: Zero Value TX received - try again!"
                    )
                    print("Zero Value TX")

        except:
            pass

