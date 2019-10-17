import time


class Timer:
    def __init__(self, stop):

        self.stop = int(stop / 10) # implement in Configuration (or extra class) to set up price iota/second

    def timer(self):

        while True:
            while self.stop >= 0:
                s = self.stop
                time_left = str(s).zfill(4)
                print(time_left + '\r')
                time.sleep(1)
                self.stop -= 1
                if self.stop <= 0:
                    print('out of time!')
                    break
            break

    def timer_load(self):

        self.start = 0

        while True:
            while self.start <= self.stop:
                s = self.start
                time_set = str(s).zfill(4)
                time.sleep(0.1)
                self.start += 1
                print(time_set)

            break
        time.sleep(1)
        print('STARTING TIMER')
        time.sleep(2)
        self.timer()
