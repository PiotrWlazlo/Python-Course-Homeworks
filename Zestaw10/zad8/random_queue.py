from random import randint


class RandomQueue:

    def __init__(self):
        self.items = []

    def __str__(self):  # podglądamy kolejkę
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        len_items = len(self.items)
        if len_items == 0:
            raise ValueError("Kolejka jest pusta.")
        maxi = randint(0, len_items - 1)
        data = self.items[maxi]
        self.items[maxi] = self.items[len_items - 1]
        del self.items[len_items - 1]
        return data


if __name__ == '__main__':
    queue_items = [1, 2, 3, 4, 5, 6, 7]
    random_queue = RandomQueue()
    for item in queue_items:
        random_queue.insert(item)

    while not random_queue.is_empty():
        print(random_queue.remove())
