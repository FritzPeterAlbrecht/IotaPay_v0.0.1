class State:
    def __init__(self, last_used_address):
        self.last_used_address = last_used_address
        self.last_used_address_compare = self.last_used_address

        self.error = "ERROR: Zero value transfer received - try again!"
        self.valtx = "Transaction received, waiting for confirmation!"
        self.confirmed = "PAYMENT CONFIRMED"
        self.timeload = "Loading timer..."
        self.timestart = "!!!STARTING TIMER!!!"
        self.service = "Device in maintenance, Service will be back in short time"

        # state prototype (0 - ready, 1 - fetching (waiting for payment), 2 - busy, -1 - error)
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

    def out_address(self):
        return self.last_used_address

    def out_last_compare(self):
        return self.last_used_address_compare

    def out_error(self):
        return self.error

    def out_valtx(self):
        return self.valtx

    def out_confirmed(self):
        return self.confirmed

    def out_timeload(self):
        return self.timeload

    def out_timestart(self):
        return self.timestart

    def out_service(self):
        return self.service
