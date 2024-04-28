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
            if 2*int(root.data[0])+1 == int(data[0]) or 2*int(root.data[0])+2 == int(data[0]):
                if not root.left:
                    root.left = self._add(root.left, data)
                else:
                    root.right = self._add(root.right, data)
            else:
                if root:
                    self._add(root.left, data)
                    self._add(root.right, data)            
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
    
    def comparePower(self, root, a, b):
        first = self.getPower(root, a)
        second = self.getPower(root, b)
        # print(first, second)
        if first == second:
            return f'{a[0]}={b[0]}'
        elif first > second:
            return f'{a[0]}>{b[0]}'
        else:
            return f'{a[0]}<{b[0]}'
        
    def getPower(self, root, i):
        root = self.breadthFirst(root, i)
        q = []
        result = 0
        q.append(root)
        while q:
            n = q.pop(0)
            # print(f'i = {i}, n = {n}')
            result += int(n.data[2])
            # print(f'i = {i}, n = {n}, result = {result}')
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return result
    
    def breadthFirst(self, root, i):
        q = []
        q.append(root)
        while q:
            n = q.pop(0)
            if int(n.data[0]) == int(i[0]):
                return n
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
    
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
T = AVLTree()
inp = input("Enter Input : ").split('/')
count = 0
all_power = 0
for i in inp[0].split():
    all_power += int(i)
    i = str(count) + ':' + i
    count += 1
    root = T.add(i)
print(all_power)
for i in inp[1].split(','):
    a = i[0]
    b = i[2]
    # print(f'a = {a}, b = {b}')
    print(T.comparePower(root, a, b))
# printTree90(root)