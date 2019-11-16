import time


class Timer:
    def __init__(self, stop, pr, state):
        self.stop = stop
        self.price = pr
        self.state = state
        self.start = 0
        self.loaded = False

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
            self.loaded = True
            self.state.set_state(4)

    # timer for the paid time in seconds
    def timer_start(self):
        #self.state.set_state(4)
        s = self.start
        time_left = str(s).zfill(4)
        print('\r' + time_left, end='')
        time.sleep(1)
        self.start -= 1
        if self.start == 0:
            self.state.set_state(5)
            print('\nout of time!')
            time.sleep(2)
            return

