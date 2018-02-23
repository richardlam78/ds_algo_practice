import sys 
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from numpy import random
from sorts import swim_sink_sort


def main():
    algos = [swim_sink_sort]
    # smaller sample to check validity
    # (except for python's sorted function)
    # NOTE: later use test functions to sort against sorted instead

    test = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,6,6,6,6,6,6,66]
    print("ORIG:", test)
    print("ORIG:", sorted(test))

    for algo in algos:
        target = test[:]
        print("\n{}: ".format(algo.__name__))
        random.shuffle(target)
        print(target)
        algo(target)
        print("{}: {}".format("GOOD" if target == sorted(test) else "BAD ",
                             target))



if __name__ == '__main__':
    main()
