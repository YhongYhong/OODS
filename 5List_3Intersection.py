class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        n = Node(data)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
    
    def isEmpty(self):
        return self.head == None
    
    def __len__(self):
        return
    
    def pop(self):
        return
    
    def index(self):
        return
    
    def __str__(self):
        if self.isEmpty():
            return "Dont have a node"
        cur, s = self.head , str(self.head.value)
        while cur.next != None:
            s += " " + str(cur.next.value) 
            cur = cur.next
        return s
    
    def search(self, data):
        if self.isEmpty():
            return "Empty cant search"
        else:
            cur = self.head
            if cur.value == data:
                return True
            else:
                while cur.next != None:
                    if cur.next.value == data:
                        return True
                    cur=cur.next
                return False
    
L = LinkedList()
inp = input("Enter edges: ").split(",")
for i in inp:
    u = i.split(">")
    # print(u[0],u[1])
    if L.isEmpty():
        L.append(u[0])
    
    # print(u[0], not L.search(u[0]))
    if not L.search(u[0]): #ทั้งสอง u0,1 ทำงานคล้ายกันแต่มีการต่อหน้าหลังไม่เหมือนกัน จึงแยกกรณี
        if int(u[0])-1 not in L:
            L_temp = LinkedList()
            L_temp.append(u[0])
        else:
            L.append(u[0])
    if not L.search(u[1]) and :
        L.append(u[1])
print(L)