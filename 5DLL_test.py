class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.c_size = 0
    
    def isEmpty(self):
        return self.head == None   
         
    def size(self):
        return self.c_size
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, ''
        while cur != None:
            s += str(cur.value) + ' '
            cur = cur.next
        return s
    
    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s
    
    def insert(self, pos, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            if pos > self.size()-1:
                self.tail.next = n
                n.previous = self.tail
                self.tail = n
            elif pos == 0 or (pos < 0 and abs(pos) > self.size()-1):
                self.head.previous = n
                n.next = self.head
                self.head = n
            else:
                count = 1
                if pos < 0:
                    cur = self.tail
                    while cur != None and abs(pos) != count:
                        cur = cur.previous
                        count += 1
                else:
                    cur = self.head
                    for i in range(pos):
                        cur = cur.next
                n.previous = cur.previous
                n.next = cur
                cur.previous.next = n
                cur.previous = n
        self.c_size += 1
    
    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.previous = self.tail
            self.tail.next = n
            self.tail = n
        self.c_size += 1
    
    def addHead(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head.previous = n
            self.head = n
        self.c_size += 1
    
    def search(self, item):
        if self.isEmpty():
            return 
        else:
            cur = self.head
            while cur != None:
                if cur.value == item:
                    return "Found"
                cur = cur.next
            return "Not Found"
    
    def index(self, item):
        if self.isEmpty():
            return
        else:
            cur, count = self.head, 0
            while cur != None:
                if cur.value == item:
                    return count
                cur = cur.next
                count += 1
            return -1
    
    def pop(self, pos):
        count = 0
        if pos >= self.c_size or pos < 0 or self.isEmpty():
            return "Out of Range"
        else:
            if pos == 0:
                self.head = self.head.next
                if not self.isEmpty():
                    self.head.previous = None
            elif pos == self.c_size-1:
                self.tail.previous.next = None
                self.tail = self.tail.previous
            else:   
                cur = self.head
                while cur != None:
                    if pos == count:
                        cur.next.previous = cur.previous
                        cur.previous.next = cur.next
                    cur = cur.next
                    count += 1
            self.c_size -= 1
            return "Success"
    
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())