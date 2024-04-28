class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)
        
class AVL_Tree:
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
            root = self.rebalances(root)
            return root
        
        self.root = _insert(self.root, data)
        return self.root
    
    def rebalances(self, root):
        if not root:
            return root
        balance = self.isBalance(root)
        # print(f'balance in class = {balance}')
        if balance == -2 :
            print("Not Balance, Rebalance!")
            if self.isBalance(root.right) == 1 :
                root.right = self.leftRotage(root.right)
            root = self.rightRotage(root)
        elif balance == 2 :
            print("Not Balance, Rebalance!")
            if self.isBalance(root.left) == -1:   
                root.left = self.rightRotage(root.left)                                         
            root = self.leftRotage(root)
        return root
    
    def leftRotage(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root
    
    def rightRotage(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root
    
    def isBalance(self,  root):
        if not root:
            return
        balance = self.height(root.left) - self.height(root.right)
        return balance
    
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
def printTree90(node, level = 0):
    if node:
        printTree90(node.right, level+1)
        print('     ' * level, node.data)
        printTree90(node.left, level+1)
    
T = AVL_Tree()
root = None
 
data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = T.insert(e)
    printTree90(root)
    print("===============")
    # print(f'height : {T.height(root)}')
