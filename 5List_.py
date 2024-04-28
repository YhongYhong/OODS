class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
            
    def __str__(self):
        return str(self.data)
    
class list:
    def __init__(self, head = None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
            
    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p