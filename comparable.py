import numpy 


class Comparable(object):

    def __init__(self, size=500):
        # create dataset of size 50 of numbers between 0 and 100 inclusive
        self.dataset = numpy.random.randint(0, 100, size)
        self.size = size

    def data(self):
        return self.dataset

    def compare(self, i, j):
        if self.dataset[i] > self.dataset[j]:
            return -1
        elif self.dataset[i] == self.dataset[j]:
            return 0
        else:
            return 1
        # maybe add some value error here


    def less(self, i, j):
        return self.compare(i, j) < 0


    def exchange(self, i, j):
        temp = self.dataset[j]
        self.dataset[j] = self.dataset[i]
        self.dataset[i] = temp

