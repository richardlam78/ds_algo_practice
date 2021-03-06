# HEAP PQ ####################################################################
# Heap PQ is a priority queue that follows the structure of a binary tree.
# For any index i, there is a parent index at i // 2 and two children
# indicies at i * 2. In other words, this queue uses heap sort.
#
# NOTE: wonder how swim and sink would work on their own to sort an array
#
# Any time that a value is added to or removed from the queue, Heap PQ
# performs the corresponding swim or sink to 'reheapify' the tree, making
# sure that the values are realigned to follow the standard mentioned
# above. And since it is in a binary tree, both insert and rmMax functions
# have O(logN).
#
class HeapPQ(object):

    def __init__(self, N=10):
        self.pq = [None] * N
        self.qcapacity = N
        self.qsize = 0


    def __resize(self, new_size):
        tempq = [None] * new_size
        for i in range(self.qsize):
            tempq[i] = self.pq[i]
        self.pq = tempq
        self.qcapacity = new_size


    def __swim(self):
        for i in reversed(range(self.qsize)):
            if (i // 2) >= 0:
                if self.pq[i] > self.pq[i // 2]:
                    temp = self.pq[i // 2]
                    self.pq[i // 2] = self.pq[i]
                    self.pq[i] = temp


    # this may need updating. refer to heapsort.
    def __sink(self):
        for i in range(self.qsize):
            if (2*i + 1) < self.qsize:
                if self.pq[i] < self.pq[2*i]:
                    temp = self.pq[2*i]
                    self.pq[2*i] = self.pq[i]
                    self.pq[i] = temp
                if self.pq[i] < self.pq[2*i + 1]:
                    temp = self.pq[2*i + 1]
                    self.pq[2*i + 1] = self.pq[i]
                    self.pq[i] = temp



    def insert(self, value):
        if self.qsize == self.qcapacity:
            self.__resize(2*self.qcapacity)
        self.qsize += 1
        self.pq[self.qsize - 1] = value
        self.__swim()


    def rmMax(self):
        if self.qsize < (self.qcapacity / 4) and self.qcapacity > 20:
            self.__resize(self.qcapacity // 2)
        heap_Max = self.pq[0]
        self.pq[0] = self.pq[self.qsize - 1]
        self.pq[self.qsize - 1] = None
        self.qsize -= 1
        self.__sink()
        return heap_Max


    def isEmpty(self):
        return True if self.qsize == 0 else False


    # FOR TESTING
    def show_pq(self):
        print(self.pq)
