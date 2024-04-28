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
        n = Node(data)
        if self.root == None:
            self.root = n
        else:
            cur = self.root
            while cur.left != None and data < cur.data:
                cur = cur.left
                if cur.right != None and data >= cur.data:
                    cur = cur.right
            while cur.right != None and data >= cur.data:
                cur = cur.right
                if cur.left != None and data < cur.data:
                    cur = cur.left
            if data < cur.data:
                cur.left = n
            else:
                cur.right = n     
        return self.root
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)