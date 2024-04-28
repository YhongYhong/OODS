class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.c_size = 0
        
    def __str__(self):
        cur, s = self.head, ''
        while cur != None:
            s += str(cur.value) + ' '
            cur = cur.next
        return s
    
    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.c_size += 1
        
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        return self.c_size
    
    def addTail(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.c_size += 1
            
    def removeHead(self):
        self.head = self.head.next
        self.c_size -= 1
    
    def removeTail(self):
        if self.size() == 1:
            self.head = self.tail = None
        else:
            cur = self.head
            while cur.next != self.tail and cur.next != None:
                cur = cur.next
            cur.next = None
        self.c_size -= 1
        
    def insert(self, item, pos):
        n = Node(item)
        if pos == 0 or (pos < 0 and abs(pos) >= self.size()):
            n.next = self.head
            self.head = n
        elif pos >= self.size():
            self.tail.next = n
            self.tail = n
        else:
            cur = self.head
            if pos > 0:
                for i in range(pos-1):
                    cur = cur.next
                n.next = cur.next
                cur.next = n
            else:
                r_pos = self.size() - abs(pos)
                for i in range(r_pos-1):
                    cur = cur.next
                n.next = cur.next
                cur.next = n
        self.c_size += 1
    
    def search(self, item):
        cur = self.head
        if self.isEmpty():
            return "Empty"
        if self.head.value == item:
            return "Found"
        else:
            while cur.next != None and cur.next.value != item:
                cur = cur.next
                if cur.next == None:
                    return "Not Found"
            return "Found"
        
    def index(self, item):
        cur = self.head
        count = 0
        if self.isEmpty():
            return "Empty"
        if self.head.value == item:
            return count
        else:
            count += 1
            while cur.next != None and cur.next.value != item:
                cur = cur.next
                count += 1
                if cur.next == None:
                    return "Dont have this item"
            return count

l = LinkedList()
l.append("A")
l.append("B")
l.append("C")
l.addTail("D")
print(l)
l.insert("1", -2)
l.removeHead()
l.removeTail()
print(l)
print(l.search("B"))
print(l.index("C"))