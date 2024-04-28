class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self, head = None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            cur = self.head
            self.size = 1
            while cur.next != None:
                cur = cur.next
                self.size += 1
            self.tail = cur
            
    def isEmpty(self):
        return self.head == None
            
    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur = self.tail
        s = str(cur.value)
        while cur.prev != None:
            cur = cur.prev
            s += " " + str(cur.value)
        return s
    
    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.size += 1
        
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, arrow = self.head, ' <-> '
        if cur.value.isalpha():
            arrow = ' > '
        while cur.next != None:
            if cur.next.value.isalpha():
                arrow = ' > '
            cur = cur.next
        cur, s = self.head , str(self.head.value)
        while cur.next != None:
            s += arrow + str(cur.next.value)
            cur = cur.next
        return s

    def __len__(self):
        return self.size

OG_L = LinkedList()
MD_L = LinkedList()
inp = input("Enter the elements of Linked list/group's size: ").split('/')

if inp[0] == '':
    print("No elements in Linked List ? OK!")
if int(inp[1]) <= 0:
    print("Group' size should be greater than 0")
else:
    elements = inp[0].split(' ') 
    for i in elements:
        OG_L.append(i)

    L2 = LinkedList()  
    cur, index = OG_L.head, 1
    L2.append(cur.value)
    if index % int(inp[1]) == 0:
        rev = L2.reverse().split(' ')
        for i in rev:
            MD_L.append(i)
        L2 = LinkedList()
    while cur.next != None:
        L2.append(cur.next.value)
        cur = cur.next
        index += 1
        if index % int(inp[1]) == 0:
            rev = L2.reverse().split(' ')
            for i in rev:
                MD_L.append(i)
            L2 = LinkedList()
    if not L2.isEmpty():
        rev = L2.reverse().split(' ')
        for i in rev:
            MD_L.append(i)
    
    print("\nOriginal Linked list:", OG_L)
    print("Modified Linked list:", MD_L)