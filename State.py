class State:
    def __init__(self, last_used_address, price):
        self.last_used_address = last_used_address
        self.price = price

        self.tx_hash = None

        self.message_strings = [
            str(
                self.last_used_address[0:41]
                + "\n"
                + self.last_used_address[42:81]
                + "\n"
                + "CHECKSUM: "
                + self.last_used_address[82:91]
            ),
            "Transaction received, waiting for confirmation!",
            "PAYMENT CONFIRMED",
            "Loading timer...",
            "!!!STARTING TIMER!!!",
            "Your rented time ended",
            "Device in maintenance, Service will be back in short time",
            "ERROR: Zero value transfer received - try again!",
            "The service is " + str(self.price) + " iota per second"
        ]

        # state prototype (0 - ready, 1 - fetching (waiting for payment), 2 - busy, 5 - error)
        self.current = None
        self.message = None

        self.set_state(0)

    def set_state(self, state):
        self.current = state
        self.message = self.message_strings[state]
        print("state is now: " + str(self.current))
