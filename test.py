#------------------------------- Search -----------------------------------------#

# def bi_search(l, r, arr, x):
#     while l <= r:
#         mid = (l+r)//2
#         if arr[mid] < x:
#             l = mid+1
#         elif arr[mid] > x:
#             r = mid-1
#         else:
#             l = r+1
        
#     return True if arr[mid] == x else False

#------------------------------- Sort -----------------------------------------#

# def bubble(l):
#     for last in range(len(l)-1, 0, -1):
#         swaped = True
#         for i in range(last):
#             if l[i] < l[i+1]:
#                 l[i], l[i+1] = l[i+1], l[i]
#                 swaped = True
            
#         if not swaped:
#             break


# def mergeSort(l, left, right):
#     center = (left+right)//2
#     if left < right:
#         mergeSort(l, left, center)
#         mergeSort(l, center+1, right)
#         merge(l, left, center+1, right)

# def merge(l, left, right, rightEnd):
#     start = left
#     leftEnd = right-1
#     result = []
#     while left <= leftEnd and right <= rightEnd:
#         if l[left] < l[right]:
#             result.append(l[left])
#             left+=1
#         else:
#             result.append(l[right])
#             right+=1
#     while left <= leftEnd:
#         result.append(l[left])
#         left+=1
#     while right <= rightEnd:
#         result.append(l[right])
#         right+=1 
#     for ele in result:
#         l[start] = ele
#         start += 1
#         if start > rightEnd:
#             break
    
# l = [5, 6, 7, 4, 3, 1, 2, 10]
# mergeSort(l, 0, len(l)-1)
# print(l)

#------------------------------- BST -----------------------------------------#

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = self.right = None
    
#     def __str__(self) -> str:
#         return str(self.data)
    
# class BST:
#     def __init__(self):
#         self.root = None
        
#     def insert(self, data):
#         def _insert(root, data):
#             if not root:
#                 return Node(data)
#             else:
#                 if data < root.data:
#                     root.left = _insert(root.left, data)
#                 else:
#                     root.right = _insert(root.right, data)
#                 return root
#         self.root = _insert(self.root, data)
#         return self.root
    
#     def levelOrder(self):
#         q = []
#         q.append(self.root)
#         while q:
#             n = q.pop(0)
#             print(n, end=' ')
#             if n.left:
#                 q.append(n.left)
#             if n.right:
#                 q.append(n.right)
    
#     def PreOrder(self,root):
#         if root:
#             print(root.data)
#             self.PreOrder(root.left)
#             self.PreOrder(root.right)
    
#     def InOrder(self,root):
#         if root:
#             self.PreOrder(root.left)
#             print(root.data)
#             self.PreOrder(root.right)
    
#     def PostOrder(self,root):
#         if root:
#             self.PreOrder(root.left)
#             self.PreOrder(root.right)
#             print(root.data)
    
# def printTree(node, level=0):
#     if node:
#         printTree(node.right, level+1)
#         print('     '*level, node.data)
#         printTree(node.left, level+1)
        
# T = BST()
# inp = [int(i) for i in input('Enter Input : ').split()]
# for i in inp:
#     root = T.insert(i)
# printTree(root)

#------------------------------- AVL -----------------------------------------#

# def insert(self, data):
#     def _insert(root, data):
#         if not root:
#             return Node(data)
#         else:
#             if data < root.data:
#                 root.left = _insert(root.left, data)
#             else:
#                 root.right = _insert(root.right, data)
#             root = self.rebalances(root)
#             return root
    
#     self.root = _insert(self.root, data)
#     return self.root

# def rebalances(self, root):
#     if not root:
#         return root
#     balance = self.isBalance(root)
#     if balance == -2:
#         if self.isBalance(root.right) == 1:
#             root.right = self.leftRotage(root.right)
#         root = self.rightRotage(root)
#     elif balance == 2:
#         if self.isBalance(root.left) == -1:
#             root.left = self.rightRotage(root.left)
#         root = self.leftRotage(root)
#         return root

# def leftRotage(self, root):
#     newroot = root.left
#     root.left = newroot.right
#     newroot.right = root
#     return newroot

# def rightRotage(self, root):
#     newroot = root.right
#     root.right = newroot.left
#     newroot.left = root
#     return newroot

# def isBalance(self, root):
#     if not root:
#         return
#     balance = self.height(root.left) - self.height(root.right)
#     return balance

# def height(self, root):
#     if not root:
#         return 0
#     return 1 + max(self.height(root.left), self.height(root.right))
