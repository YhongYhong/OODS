class Queue:
    def __init__(self, q = None):
        if q == None:
            self.item = []
        else:
            self.item = q
    def enQueue(self, i):
        self.item.append(i)
    def deQueue(self):
        return self.item.pop(0)
    def isEmpty(self):
        return self.item == []
    def size(self):
        return len(self.item)

class AVLTree():
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
            self.check = False
        
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
        if balance == -2 : 
            if x.right.balanceValue() == 1 :
                x.right = self.leftRotage(x.right)
            x = self.rightRotage(x)
        elif balance == 2 : 
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
     
        
    def __str__(self) -> str:
        lines = AVLTree._build_tree_string(self.root, 0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

    def _build_tree_string(
        root: AVLNode,
        curr_index: int,
        include_index: bool = False,
        delimiter: str = "-") :

        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if include_index:
            node_repr = "{}{}{}".format(curr_index, delimiter, root.data)
        else:
            node_repr = str(root.data) + ":" + str(root.height) ## add for other value to display

        new_root_width = gap_size = len(node_repr)

        l_box, l_box_width, l_root_start, l_root_end = AVLTree._build_tree_string(root.left, 2 * curr_index + 1, include_index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = AVLTree._build_tree_string(root.right, 2 * curr_index + 2, include_index, delimiter)
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(" " * (l_root + 1))
            line1.append("_" * (l_box_width - l_root))
            line2.append(" " * l_root + "/")
            line2.append(" " * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        line1.append(node_repr)
        line2.append(" " * new_root_width)

        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append("_" * r_root)
            line1.append(" " * (r_box_width - r_root + 1))
            line2.append(" " * r_root + "\\")
            line2.append(" " * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)

        return new_box, len(new_box[0]), new_root_start, new_root_end

    def inOrder(self):
        print("AVLTree in-order : ",end="")
        self._inOrder(self.root)
        print()
            
    def _inOrder(self, root):
        if root is not None:
            self._inOrder(root.left)
            print(root, end = ' ')
            self._inOrder(root.right) 
    
    def postOrder(self):
        print("AVLTree post-order : ",end="")
        self._postOrder(self.root)
        print()
            
    def _postOrder(self, root):
        if root is not None:
            self._postOrder(root.left)
            self._postOrder(root.right)
            print(root, end = ' ')
    
    def delete(self, data) :
        self.root = self._delete(self.root, data)
  
    def _delete(self, root, key) :
        if root is None : return root
        if int(key) < int(root.data) :
            root.left = self._delete(root.left, key)
        elif int(key) > int(root.data) :
            root.right = self._delete(root.right, key)
        else :
            if root.left is None or root.right is None :
                root = root.left if root.right is None else root.right
            else :
                temp = root.left
                while temp.right is not None :
                    temp = temp.right
                root.data = temp.data
                root.left = self._delete(root.left, temp.data)
            root = self.rebalanceS(root)         
        return root

    def replacenodelevelOrder(self,list):
        q = Queue()
        q.enQueue(self.root)
        while q.isEmpty() is not True :
            n = q.deQueue()
            if n.left is not None:
                if n.left.height == 0 : 
                    n.left.data = list[0]
                    list = list[1:] 
                q.enQueue(n.left)
            if n.right is not None:
                if n.right.height == 0 : 
                    n.right.data = list[0]
                    list = list[1:]
                q.enQueue(n.right)
    
    def tonmaiyab(self):
        self._tonmaiyab(self.root,1,self.root.height)

    def _tonmaiyab(self,root,height,maxheight) :
        if height > maxheight or root is None:
            return
        if root.height == height:
            if root.right is None:
                root.data = root.left.data 
            else :
                if root.right.data >= root.left.data:
                    root.data = root.left.data 
                else :
                    root.data = root.right.data 
            self._tonmaiyab(self.root,height + 1,maxheight)
        else : 
            self._tonmaiyab(root.left,height,maxheight)
            if root.right : self._tonmaiyab(root.right,height,maxheight)
    

    def sumtree(self):
        sum = 0
        q = Queue()
        q.enQueue(self.root)
        while q.isEmpty() is not True :
            n = q.deQueue()
            sum += n.data
            if n.left is not None:
                if n.right is not None:
                    if n.right.data >= n.left.data:
                        n.right.data -= n.left.data
                        n.left.data = 0
                    else :
                        n.left.data -= n.right.data
                        n.right.data = 0
                else :
                    n.left.data = 0
                q.enQueue(n.left)
            if n.right is not None:
                q.enQueue(n.right)
        return sum


avl = AVLTree()
inp = input("Enter Input : ").split("/")
amount = int(inp[0])
value = [int(i) for i in inp[1].split()]
if len(value) == amount//2 + 1 :
    for i in range(amount):
        root = avl.add(i)
    avl.replacenodelevelOrder(value)
    avl.tonmaiyab()
    # print(avl)
    print(avl.sumtree())
    # print(avl)
else : print("Incorrect Input")