from numsort import *
import math


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

def insertsort(L, left, right):
    for i in range(right, left, -1):   # ustawiam wartownika
        if L[i-1] > L[i]:
            swap(L, i-1, i)
    for i in range(left+2, right+1):
        j = i
        item = L[i]
        while item < L[j-1]:   # robimy miejsce na item
            L[j] = L[j-1]
            j = j-1
        L[j] = item


def bucketsort(L):
    bucket = [[],[],[],[],[],[],[],[],[],[]]
    div = math.ceil((max(L)+1)/len(bucket))
    for i in L:
        x = math.floor(i/div)
        bucket[x].append(i)
    for i in bucket:
        insertsort(i, 0, len(i)-1)
    arr = [item for sublist in bucket for item in sublist]
    return arr


def neg_bucketsort(L):
    pos = []
    neg = []
    for i in L:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    L = bucketsort(neg)
    E = bucketsort(pos)
    L.extend(E)
    return L
