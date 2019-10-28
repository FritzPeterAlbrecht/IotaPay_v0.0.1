import time
#from GUI import CallbackObject


class Timer:
    def __init__(self, stop, pr, parent=None):
        #self.call = CallbackObject(parent=parent)
        self.stop = int(stop / pr)

    # timer for the paid time in seconds
    def timer(self):

        while True:
            while self.stop >= 0:
                s = self.stop
                time_left = str(s).zfill(4)
                print('\r' + time_left, end='')
                time.sleep(1)
                self.stop -= 1
                #self.call.triggerSignal()
                if self.stop == 0:
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
                time.sleep(0.1)
                self.start += 1
                #self.call.triggerSignal()
                print('\r' + time_set, end='')

            break
        time.sleep(1)
        print('\nSTARTING TIMER')
        time.sleep(1)
        self.timer()
