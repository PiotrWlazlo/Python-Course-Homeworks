import random


def create_list(n=100, k=10):
    l = [random.randint(0, k - 1) for l in range(n)]
    return l


def random_number(k=10):
    return random.randint(0, k - 1)


def linear_search(L, y, left=0, right=None):
    if right is None:
        right = len(L) - 1
    index_list = []
    i = left
    while i <= right:
        if L[i] == y:
            index_list.append(i)
        i += 1
    return index_list


def search_random_number(n=100, k=10):
    L = create_list(n, k)
    y = random_number(k)
    return y, linear_search(L, y)


if __name__ == '__main__':
    y, L = search_random_number(100, 10)
    print("Draw number: " + str(y))
    print("Number exist on positions: " + str(L))
