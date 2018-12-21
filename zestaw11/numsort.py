import random as r
import math as m


def random_ints(N):
    return r.sample(range(N),N)


def almost_sorted_ints(N):
    weights = [2 ** i for i in range(N,0,-1)]
    arr = list(range(N))
    arr2 = []
    while len(arr) > 0:
        arr2.append(r.choices(arr, weights)[0])
        arr.remove(arr2[len(arr2) - 1])
        weights.pop(0)
    #print(arr2)
    return arr2



def invert_almost_sorted_ints(N):
    weights = [2 ** i for i in range(N)]
    arr = list(range(N))
    arr2 = []
    while len(arr) > 0:
        arr2.append(r.choices(arr, weights)[0])
        arr.remove(arr2[len(arr2) - 1])
        weights.pop(0)
    return arr2

def gauss_floats(N):
    arr = [r.gauss(0, 1) for i in range(N)]
    return arr


def random_k_ints(N):
    arr = [r.randint(0,m.floor(m.sqrt(N))) for i in range(N)]
    return arr
