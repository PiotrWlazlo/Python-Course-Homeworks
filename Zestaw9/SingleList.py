class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self, *arguments):
        self.length = 0
        self.head = None
        self.tail = None
        for i in arguments:
            self.push_head(i)


    def push_head(self,value):
        node = Node(value)
        if self.is_empty() == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1


    def __str__(self):
        node = self.head
        L = []
        while node != self.tail:
            L.append(node.data)
            node = node.next
        print(L)
        return L

    def size(self):
        return self.length

    def is_empty(self):
        if self.length == 0:
            return True

    def pop_head(self):
        if self.is_empty():
            raise Exception("Nothing to delete")
        node = self.head
        self.head = node.next
        self.length -= 1
        if self.is_empty():
            self.tail = None
        return node

    def reverse(self):
        if self.is_empty():
            raise Exception("Nothing to delete")
        node = self.head
        prev = None
        next = None
        while node != self.tail:
            next = node.next
            node.next = prev
            prev = node
            node = next
        self.tail = self.head
        self.head = prev
        return self

lista = SingleList(6,5,4,3,2,1)
lista.__str__()
#print("Stara lista")
#lista.__str__()
lista.reverse().__str__()
#print("Nowa lista")
#lista.__str__()

