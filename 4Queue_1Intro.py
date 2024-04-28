class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def push(self, i):
        self.items.append(i)
        
    def pop(self):
        return print(self.items.pop(0), '0')
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def Qing(i):
    q = Queue()
    for y in i:
        if y[0] == 'E':
            q.push(y[2:])
            print(q.size())
        elif y[0] == 'D':
            if not q.isEmpty(): q.pop()
            else: print('-1')
            
    if not q.isEmpty():
        remain = ''
        for z in q.items:
            remain += z+' '
        return remain
    else: return ('Empty')
    
inp = input('Enter Input : ').split(',')
# a = Queue(inp)
print(Qing(inp))
