class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
        
        def __str__(self):
            return str(self.data)
        
        def setHeight(self):
                a = self.getHeight(self.left)
                b = self.getHeight(self.right)
                self.height = 1 + max(a,b)
                return self.height
            
        def getHeight(self, node):
            return -1 if node == None else node.height
            
        def balanceValue(self):
            return self.getHeight(self.left) - self.getHeight(self.right)
    
    def __init__(self, root = None):
        self.root = None if root is None else root
    
    def add(self, data):
        self.root = self._add(self.root, data)
        return self.root

    def _add(self, root, data):
        if root is None:
            return self.AVLNode(data)
        else:
            if int(data) < int(root.data):
                root.left = self._add(root.left, data)
            else:
                root.right = self._add(root.right, data)
            root = self.rebalanceS(root)                
            return root
    
    def rebalanceS(self, x):
        if x == None:
            return x
        balance = x.balanceValue()
        print(f'balance in class = {balance}')
        if balance == -2 :
            print("Not Balance, Rebalance!")
            if x.right.balanceValue() == 1 :
                x.right = self.leftRotage(x.right)
            x = self.rightRotage(x)
        elif balance == 2 :
            print("Not Balance, Rebalance!")
            if x.left.balanceValue() == -1:   
                x.left = self.rightRotage(x.left)                                         
            x = self.leftRotage(x)
        x.setHeight()
        return x 
  
    def leftRotage(self, x) :
        y = x.left
        x.left = y.right
        y.right = x
        x = y
        x.right.setHeight()
        x.setHeight()
        return x
    
    def rightRotage(self, x) :
        y = x.right
        x.right = y.left
        y.left = x    
        x = y
        x.left.setHeight()
        x.setHeight()
        return x
    
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVLTree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.add(e)
    printTree90(root)
    # print(f'balance out class = {root.balanceValue()}')
    print("===============")
