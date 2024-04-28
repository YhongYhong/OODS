class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def push(self, i):
        self.items.append(i)
        # self.size += 1
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == [] # or len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        s = 'stack of ' + str(self.size()) + ' items : '
        for ele in self.items:
            s += str(ele)+''
        return s
   
i = ['a', 'b', 'c'] 
a = Stack(i)
print(a)
print(a.peek())