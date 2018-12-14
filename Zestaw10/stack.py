class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.size == self.n:
            raise ValueError("Stos jest pełny.")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.n == 0:
            raise ValueError("Stos jest pusty.")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data
