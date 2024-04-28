class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        cur, s = self.head, str(self.head.value) + ' '
        while cur.next != None:
            cur = cur.next
            s += str(cur.value) + ' '
        return s

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        if self.isEmpty():
            return 0
        cur, count = self.head, 1
        while cur.next != None:
            cur = cur.next
            count += 1
        return count
    
    def search(self, item):
        pass
    
    def index(self, item):
        cur, index = self.head, 0
        if cur.value == item:
            return index
        while cur.next != None:
            cur = cur.next
            index += 1
            if cur.value == item:
                return index
        return -1
    
    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
            
    def remove(self, item):
        pass
    
    def pop(self, pos):
        pass
            
L = LinkedList()
print("***Railway on route***")
inp = input("Input Station name/Source, Destination, Direction(optional): ").split('/')
station_name, direction = inp[0].split(','), inp[1].split(',')

for i in station_name:
    L.append(i)

start = L.index(direction[0])
end = L.index(direction[1]) 
f_distance = end-start
if f_distance < 0: f_distance = f_distance + L.size()
b_distance = (L.size()-end)+start

s1 = 'Forward Route: '
cur = L.head
if L.head.value == direction[0]:
    s1 += str(cur.value)
else:
    while cur.next.value != direction[0]:
        cur = cur.next
    s1 += str(cur.next.value)
    cur = cur.next
while cur.next.value != direction[1]:
    s1 += '->' + str(cur.next.value)
    cur = cur.next
    if cur.next == None:
        cur = L.head
        s1 += '->' + str(cur.value)
s1 +=  '->' + str(cur.next.value)

s2 = 'Backward Route: '
cur = L.head
if L.head.value == direction[0]:
    s2 += str(cur.value)
else:
    while cur.next.value != direction[0]:
        cur = cur.next
    s2 += str(cur.next.value)
    cur = cur.next
while cur.prev != None and cur.prev.value != direction[1]:
    s2 += '->' + str(cur.prev.value)
    cur = cur.prev
    if cur == L.head: break
cur = L.tail
s2 += '->' + str(cur.value)
if L.tail.value != direction[1]:
    while cur.prev.value != direction[1]:
        s2 += '->' + str(cur.prev.value)
        cur = cur.prev
    s2 += '->' + str(cur.prev.value)

if len(direction) == 3:
    if direction[2] == 'F':
        print(f'{s1},{f_distance}')
    elif direction[2] == 'B':
        print(f'{s2},{b_distance}')
else:
    if f_distance < b_distance:
        print(f'{s1},{f_distance}')
    elif  b_distance < f_distance:
        print(f'{s2},{b_distance}')
    else:
        print(f'{s1},{f_distance}')
        print(f'{s2},{b_distance}')