class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
            self.parent = None
        
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

    def _add(self, root, data,):
        if root is None:
            return self.AVLNode(data)
        else:
            if int(data) < int(root.data):
                root.left = self._add(root.left, data)
            else:
                root.right = self._add(root.right, data)
            root = self.rebalanceS(root)            
        return root
        
    def parenting(self, root, pre_root = None):
        if root != None:
            self.parenting(root.left, root)
            if root.left:
                root.left.parent = root
            if root.right:
                root.right.parent = root
            self.parenting(root.right, root)
        
    def burn(self, root, data):
        node = self.searchRoot(root, int(data))
        if not node:
            print(f"There is no {data} in the tree.")
            return 
        burned = []
        will_burn = [node]
        next = []
        while will_burn:
            for i in will_burn:
                if i not in burned:
                    burned.append(i)
                    print(i.data, end=' ')
                    if i.left and i.left not in burned:
                        next.append(i.left)
                    if i.right and i.right not in burned:
                        next.append(i.right)
                    if i.parent and i.parent not in burned:
                        next.append(i.parent)
            will_burn = []
            for i in next:
                will_burn.append(i)
            next = []
            print()
    
    def searchRoot(self, root, data):
        q = [root]
        while q:
            cur = q.pop(0)
            if cur.data == data:
                return cur
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
                
    def breadthFirst(self, root):
        q = []
        q.append(root)
        while q:
            n = q.pop(0)
            print(f'root:{n}, pr:{n.parent} ||',end=' ')
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
    
    def rebalanceS(self, x):
        if x == None:
            return x
        balance = x.balanceValue()
        # print(f'balance in class = {balance}')
        if balance == -2 :
            # print("Not Balance, Rebalance!")
            if x.right.balanceValue() == 1 :
                x.right = self.leftRotage(x.right)
            x = self.rightRotage(x)
        elif balance == 2 :
            # print("Not Balance, Rebalance!")
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

data = input("Enter node and burn node : ").split('/')
for e in data[0].split():
    root = myTree.add(int(e))
myTree.parenting(myTree.root)
myTree.burn(root, int(data[1]))