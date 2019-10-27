import time


class Timer:
    def __init__(self, stop, pr):
        #self.price = pr
        self.stop = int(stop / pr) # implement in Configuration to set up price iota/second

    # timer for the paid time in seconds
    def timer(self):

        while True:
            while self.stop >= 0:
                s = self.stop
                time_left = str(s).zfill(4)
                print('\r' + time_left, end='')
                time.sleep(1)
                self.stop -= 1
                if self.stop <= 0:
                    print('\nout of time!')
                    break
            break

    # run up timer depending on amount paid
    def timer_load(self):

        self.start = 0

        while True:
            while self.start <= self.stop:
                s = self.start
                time_set = str(s).zfill(4)
                time.sleep(0.2)
                self.start += 1
                print('\r' + time_set, end='')

            break
        time.sleep(1)
        print('\nSTARTING TIMER')
        time.sleep(1)
        self.timer()
