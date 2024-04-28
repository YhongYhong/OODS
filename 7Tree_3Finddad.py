class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r,data):
    if data == r.data:
        return "None Because " + str(data) + " is Root"
    else:
        cur = r
        while cur.left or cur.right:
            if data < cur.data:
                if cur.left and data == cur.left.data:
                    return cur.data
                cur = cur.left
            else:
                if cur.right and data == cur.right.data:
                    return cur.data
                cur = cur.right
        return "Not Found Data"

# def father(r,data):
#     #code here
#     if r.data == data:
#         return f'None Because {r} is Root'
#     cur = r
#     while cur.left or cur.right:
#         if data < cur.data:
#             if cur.left.data == data:
#                 return cur.data
#             cur = cur.left
#         else:
#             if cur.right.data == data:
#                 return cur.data
#             cur = cur.right

#     return 'Not Found Data'
        

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(int(e))
printTree90(tree.root)
print(father(tree.root,int(data[1])))