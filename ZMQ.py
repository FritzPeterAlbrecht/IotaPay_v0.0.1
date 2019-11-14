import sys
import zmq


class ZMQ:
    def __init__(self, last_used_address, state, ic):
        # > Init ZMQ!
        self.last_used_address = last_used_address
        self.ZMQContext = zmq.Context()
        self.ZMQSocket = self.ZMQContext.socket(zmq.SUB)
        self.ZMQSocket.connect("tcp://zmq.devnet.iota.org:5556")
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, "tx")
        self.ZMQSocket.setsockopt_string(zmq.SUBSCRIBE, "sn")

        self.ic = ic

        self.value = 0
        self.state = state

    def listen(self):
        # > Process

        try:
            zmq_response = self.ZMQSocket.recv(flags=zmq.NOBLOCK).decode().split()
            topic = str(zmq_response[0])
            address = str(zmq_response[2])
            value = int(zmq_response[3])

            self.last_used_address = self.last_used_address[0:81]

            # catch tx for actual address
            if topic == 'tx':
                if address == self.last_used_address:
                    print('Topic is:', topic)
                    if value != 0:
                        self.state.set_state(1, self.state.states[0])
                        print('Value TX incoming')
                    else:
                        self.state.set_state(5, self.state.states[5])

            # catch confirmation message for actual address
            if topic == 'sn':
                tx_trytes = zmq_response[2]
                print(tx_trytes)
                trytes_response = self.ic.get_trytes(tx_trytes)

                print(trytes_response)
                # if address == self.last_used_address:
                #     print('Topic is:', topic)
                #     if value != 0:
                #         self.state.set_state(1, self.state.states[1])
                #         print('CONFIRMED')

        except:
            pass

