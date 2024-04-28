class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
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

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.previous = self.tail
            self.tail.next = n
            self.tail = n

    def addHead(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.previous = n
            self.head = n

    def insert(self, pos, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
            return
        r_pos = self.size() + pos
        cur = self.head
        if (pos <= 0 and abs(pos) > self.size()) or pos == 0:
            n.next = self.head
            self.head.previous = n
            self.head = n
        elif pos >= self.size():
            self.tail.next = n
            n.previous = self.tail
            self.tail = n
        else:
            if pos < 0:
                for i in range(r_pos):
                    cur = cur.next
            else:
                for i in range(pos):
                    cur = cur.next
            n.previous = cur.previous
            n.next = cur
            cur.previous.next = n
            cur.previous = n
        

    def search(self, item):
        cur = self.head
        if cur.value == item:
            return 'Found'
        while cur.next != None:
            if cur.next.value == item:
                return 'Found'
            cur = cur.next
        return 'Not Found'

    def index(self, item):
        ind = 0
        cur = self.head
        if cur.value == item:
            return ind
        while cur.next != None:
            ind += 1
            if cur.next.value == item:
                return ind
            cur = cur.next
        ind = -1
        return ind
    
    def size(self):
        if self.head == None:
            count = 0
            return count
        cur = self.head
        count = 1
        while cur.next != None:
            count += 1
            cur = cur.next
        return count

    def pop(self, pos):
        if pos >= self.size() or pos < 0:
            return 'Out of Range'
        else:
            cur = self.head
            if pos == 0:
                self.head = self.head.next
            elif pos == self.size()-1:
         
                self.tail = self.tail.previous
                self.tail.next = None
            else:
                for i in range(pos):
                    cur = cur.next
                cur.previous.next = cur.next
                cur.next.previous = cur.previous
            return 'Success'
        
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