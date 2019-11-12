class Output:
    def __init__(self, last):
        self.last = last
        self.last_compare = self.last
        self.last = str(self.last[0:41] + '\n' + self.last[
                        42:81] + '\n' + 'CHECKSUM: ' + self.last[82:91])
        self.error = 'ERROR: Zero value transfer received - try again!'
        self.valtx = 'Transaction received, waiting for confirmation!'
        self.confirmed = 'PAYMENT CONFIRMED'
        self.timeload = 'Loading timer...'
        self.timestart = '!!!STARTING TIMER!!!'
        self.service = 'Device in maintenance, Service will be back in short time'

    def out_address(self):
        return self.last

    def out_last_compare(self):
        return self.last_compare

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
