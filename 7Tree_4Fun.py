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
        
        def _insert(root, data):
            if not root:
                return Node(data)
            else:
                if data < root.data:
                    root.left = _insert(root.left, data)
                else:
                    root.right = _insert(root.right, data)
            return root
        
        self.root = _insert(self.root, data)
        return self.root
    
    def preOrder(self, root):
        if root:
            print(root.data,end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)
            
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data,end=' ')
            self.inOrder(root.right)
            
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data,end=' ')
            
    def breadthFirst(self, root):
        q = []
        q.append(root)
        while q:
            n = q.pop(0)
            print(n,end=' ')
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
    
    def printTree(self, node, level = 0):
        if node:
            self.printTree(node.right, level+1)
            print('     ' * level, node)
            self.printTree(node.left, level+1)
            
T = BST()
inp = input("Enter Input : ").split()
for i in inp:
    root = T.insert(int(i))
T.printTree(root)
print("Preorder : ",end='' )
T.preOrder(root)
print("\nInorder : ",end='' )
T.inOrder(root)
print("\nPostorder : ",end='' )
T.postOrder(root)
print("\nBreadth : ",end='' )
T.breadthFirst(root)