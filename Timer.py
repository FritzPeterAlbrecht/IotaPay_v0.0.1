import time


class Timer:
    def __init__(self):

        self.stop = 5

    def timer(self):

        while True:
            while self.stop >= 0:
                m, s = divmod(self.stop, 60)
                h, m = divmod(m, 60)
                time_left = str(h).zfill(2) + ':' + str(s).zfill(2)
                print(time_left + "\r")
                time.sleep(1)
                self.stop -= 1
                if self.stop <= 0:
                    print('out of time!')
                    break
            break
