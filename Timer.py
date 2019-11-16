import time


class Timer:
    def __init__(self, stop, pr):
        self.stop = stop
        self.price = pr
        self.start = 0

    # run up timer depending on amount paid
    def timer_load(self, stop):
        self.stop = int(stop/self.price)
        s = self.start
        time_set = str(s).zfill(4)
        time.sleep(0.1)
        self.start += 1
        print('\r' + time_set, end='')
        if s == self.stop:
            time.sleep(1)
            print('\nSTARTING TIMER')
            time.sleep(1)
            self.timer()

    # timer for the paid time in seconds
    def timer(self):

        s = self.start
        time_left = str(s).zfill(4)
        print('\r' + time_left, end='')
        time.sleep(1)
        self.start -= 1
        if self.start == 0:
            print('\nout of time!')
