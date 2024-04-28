class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        
    def enQueue(self, i):
        self.items.append(i)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root
    
    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data > root.data:
            root.right = self._insert(root.right, data)
        else:
            root.left = self._insert(root.left, data)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1) 
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def search(self, node, data):
        if data == node.data:
            return node
        elif data < node.data:
            if node.left:
                return self.search(node.left, data)
            else:
                return str(data)+' is not found in the BST'
        else:
            if node.right:
                return self.search(node.right, data)
            else:
                return str(data)+' is not found in the BST'

    def preOrder(self, node):
        if node:
            print(node, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node, end=' ')
            self.inOrder(node.right)
    
    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node, end=' ')

    def levelOrder(self):
        q = Queue()
        q.enQueue(self.root)
        while not q.isEmpty():
            n = q.deQueue()
            print(n, end=' ')
            if n.left:
                q.enQueue(n.left)
            if n.right:
                q.enQueue(n.right)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

print('Preorder : ', end='')
T.preOrder(root)
print(f'\nInorder : ', end='')
T.inOrder(root)
print(f'\nPostorder : ', end='')
T.postOrder(root)
print(f'\nBreadth : ', end='')
T.levelOrder()