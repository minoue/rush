import time


def timer(func):

    def __timeWrapper(*args):

        t = time.time()
        func()
        print t - time.time()

    return __timeWrapper
