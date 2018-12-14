class PriorityQueue:

    def __init__(self):
        self.items = []

    def __str__(self):  # podglądamy kolejkę
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        len_items = len(self.items)
        if len_items == 0:
            raise ValueError("Kolejka jest pusta.")
        for i in range(1, len_items):
            if self.items[i] > self.items[maxi]:
                maxi = i
        data = self.items[maxi]
        self.items[maxi] = self.items[len_items - 1]
        del self.items[len_items - 1]
        return data
