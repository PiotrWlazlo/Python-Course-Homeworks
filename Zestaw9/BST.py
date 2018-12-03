class Node:

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        #self.insert(data)   #initialize root

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:  # na prawo
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:  # na lewo
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass  # ignoruję duplikaty

    def count(self):
        return self.count

    def bst_max(self, top):
        if top is None:
            raise ValueError("No tree")
        if top.right is None:
            return top.data
        while top.right:
            top = top.right
        return top.data

    def bst_min(self, top):
        if top is None:
            raise ValueError("No tree")
        if top.left is None:
            return top.data
        while top.left:
            top = top.left
        return top.data


root = Node(4)
root.insert(7)
root.insert(9)
root.insert(2)
root.insert(10)
root.insert(6)
root.insert(7)
print(root.bst_max(root))
print(root.bst_min(root))
