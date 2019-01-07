import math

def binary_search_recursion(L, left, right, y):
    if len(L) == 0:
        raise ValueError("Empty array")
    if left > right:
        return None
    k = math.floor((left + right) / 2)
    if L[k] == y:
        return k
    if y < L[k]:
        return binary_search_recursion(L, left, k - 1, y)
    else:
        return binary_search_recursion(L, k + 1, right, y)
