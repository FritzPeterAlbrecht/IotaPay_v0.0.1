class State:
    def __init__(self, config, ic, qr):
        self.ic = ic
        self.qr = qr

        self.last_used_address = self.ic.json.last_used_address()
        self.price = config.getPrice()

        self.tx_hash = None
        self.user_credit = 0

        self.message_strings = [
            "",
            "Transaction received, waiting for confirmation!",
            "PAYMENT CONFIRMED",
            "Working",
            "Timer ended",
            "Device in maintenance, Service will be back in short time",
            "ERROR: Zero value transfer received - try again!",
            "The service is " + str(self.price) + " iota per second",  # not dynamic!
        ]

        # state prototype (0 - ready, 1 - fetching (waiting for payment), 2 - busy, 5 - error)
        self.current = None
        self.message = None

        self.set(0)
        self.update_qr()

    def set(self, state):
        self.current = state
        print("state is now: " + str(self.current))

        # quick fix
        if state == 0:
            self.message = str(
                self.last_used_address[0:41]
                + "\n"
                + self.last_used_address[42:81]
                + "\n"
                + "CHECKSUM: "
                + self.last_used_address[82:91]
            )

        else:
            self.message = self.message_strings[self.current]

    def next_address(self):
        self.ic.generate_new_address()
        self.last_used_address = self.ic.json.last_used_address()
        print(self.last_used_address)

    def update_qr(self):
        self.qr.qrCode(self.last_used_address)
