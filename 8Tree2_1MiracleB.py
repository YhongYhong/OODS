class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        
        def _insert(root, data):
            if not root:
                print('*')
                return Node(data)
            else:
                if data < root.data:
                    print('L',end='')
                    root.left = _insert(root.left, data)
                else:
                    print('R',end='')
                    root.right = _insert(root.right, data)
            return root
        
        self.root = _insert(self.root, data)
        return self.root
    
    def printTree(self, node, level = 0):
        if node:
            self.printTree(node.right, level+1)
            print('     ' * level, node.data)
            self.printTree(node.left, level+1)
    
T = BST()
inp = input("Enter Input : ").split()
for i in inp:
    root = T.insert(int(i))
# T.printTree(root)
