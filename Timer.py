import time


class Timer:
    def __init__(self, state):
        self.state = state
        self.duration = 0

    # run up timer depending on amount paid
    def setup(self):
        self.paid_time = int(self.state.user_credit / self.state.price)
        self.duration += 1
        if self.duration == self.paid_time:
            self.state.set(3)

    # timer for the paid time in seconds
    def update(self):
        self.duration -= 1
        if self.duration == 0:
            self.state.set(4)
