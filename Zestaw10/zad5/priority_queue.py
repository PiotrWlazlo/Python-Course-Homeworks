class PriorityQueue:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0   # pierwszy wolny indeks
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def insert(self, data):
        if self.n == self.size:
            raise ValueError("Kolejka jest pelna.")
        self.items[self.n] = data
        self.n += 1

    def remove(self):
        if self.n == 0:
            raise ValueError("Kolejka jest pusta.")
        maxi = 0
        for i in range(self.n):
            if self.items[i] > self.items[maxi]:
                maxi = i
        # Etap 2 - usuwanie elementu.
        self.n -= 1
        data = self.items[maxi]
        self.items[maxi] = self.items[self.n]
        self.items[self.n] = None   # usuwamy referencję
        return data
