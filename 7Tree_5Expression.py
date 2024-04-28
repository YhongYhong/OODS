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
        self.root = self._insert_postfix(data, self.root)
        return self.root
    
    def _insert(self, data, root):
        n = Node(data)
        if root is None:
            return n
        else:
            if data < root.data:
                root.left = self._insert(data, root.left)
            else:
                root.right = self._insert(data, root.right)
        return root
    
    def _insert_postfix(self, data, root):
        if root is None:
            return Node(data)
        else:
            if root.right != None and (self.is_full_alpha(root.right) or root.right.data.isalpha()):
                root.left = self._insert_postfix(data, root.left)
            else:
                root.right = self._insert_postfix(data, root.right)
            return root
        
    def is_full_alpha(self, root):
        if root.right and root.left:
            if root.right.data.isalpha() and root.left.data.isalpha():
                return True
            elif root.left.data.isalpha():
                return self.is_full_alpha(root.right)
            else:
                return self.is_full_alpha(root.left)
        else:
            return False
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def postOrder(self, root, s = ''):
        if root:
            if root.left is not None or root.right is not None:
                print('(',end='')
            self.postOrder(root.left)
            print(root.data,end='')
            self.postOrder(root.right)
            if root.left is not None or root.right is not None:
                print(')',end='')
    
    def preOrder(self, root):
        if root:
            print(root.data,end='')
            self.preOrder(root.left)
            self.preOrder(root.right)
            
def PostToIn(l):
    stack = []
    for i in l:
        if i.isalnum():
            stack.append(i)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expression = f"({operand1}{i}{operand2})"
            stack.append(expression)
    return stack[0]

# def PostToPre(l):
#     stack = []
#     for i in l:
#         if i.isalnum():
#             stack.append(i)
#         else:
#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             expression = f"{i}{operand1}{operand2}"
#             stack.append(expression)
#     return stack[0]
               
T = BST()
inp = [i for i in input("Enter Postfix : ")]
# infix_inp = PostToIn(inp)
# prefix_inp = PostToPre(inp)
inp.reverse()
for i in inp:
    root = T.insert(i)
print("Tree :")
T.printTree(root)
print('--------------------------------------------------')
print("Infix : ",end='')
T.postOrder(root)
print("\nPrefix : ",end='')
T.preOrder(root)