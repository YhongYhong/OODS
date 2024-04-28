class node:
    def __init__(self, data):
        self.value = data
        self.next = None
        
class Snode:
    def __init__(self, data):
        self.value = data
        self.next = None
        
class link:
    def __init__(self):
        self.head_node = None
        
    def next_node(self, data):
        if self.head_node != None and self.search(data):
            return 
        if self.head_node == None:
            self.head_node = data
        else:
            cur = self.head_node
            while cur.next != None:
                cur = cur.next
            cur.next = data
        
    def search(self, data):
        if self.head_node.value == data.value:
            return True
        cur = self.head_node
        while cur.next != None:
            if cur.next.value == data.value:
                return True
            cur = cur.next
        return False
        
    def next_secondary_node(self, n, data):
        cur = self.head_node
        if cur.value[0] != n:
            while cur.next != None:
                cur = cur.next
                if cur.value[0] == n:
                    break
        if cur.next == None or cur.next.value[0] != n:
            data.next = cur.next
            cur.next = data
        else:
            while cur.next != None and cur.next.value[0] == n:
                cur = cur.next
            data.next = cur.next
            cur.next = data
        
    def show_all(self):
        if self.head_node == None:
            return "Empty"
        else:
            cur, s = self.head_node , self.head_node.value + " : "
            while cur.next != None:
                # print(s)
                if len(cur.next.value) == 1:
                    cur = cur.next
                    s += "\n" + cur.value + " : "
                while cur.next != None and len(cur.next.value) == 2:
                    s += cur.next.value + ","
                    cur = cur.next
            print(s)
        
inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],Snode(h[1]))
l.show_all()