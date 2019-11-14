class State:
    def __init__(self, last_used_address):
        self.last_used_address = last_used_address
        self.last_used_address_compare = self.last_used_address

        self.states = ["Transaction received, waiting for confirmation!",
                       "PAYMENT CONFIRMED",
                       "Loading timer...",
                       "!!!STARTING TIMER!!!",
                       "Device in maintenance, Service will be back in short time",
                       "ERROR: Zero value transfer received - try again!"]

        # state prototype (0 - ready, 1 - fetching (waiting for payment), 2 - busy, 5 - error)
        self.current = None
        self.message = None

        self.set_state(
            0,
            str(
                self.last_used_address[0:41]
                + "\n"
                + self.last_used_address[42:81]
                + "\n"
                + "CHECKSUM: "
                + self.last_used_address[82:91]
            ),
        )

    def set_state(self, state, message):
        self.current = state
        self.message = message
        print("state is now: " + str(self.current))
