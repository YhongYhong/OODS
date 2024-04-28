class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def enQueue(self, i):
        self.items.append(i)
        
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
inp = input('Enter Input : ').split('/')
left = [x for x in inp[0].split()]
right = [x for x in inp[1].split(',')]
main = Queue(left)

for i in range(len(right)):
    if right[i][0] == 'E':
        main.enQueue(right[i][2:])
    else:
        main.deQueue()
        
if len(main.items) == len(set(main.items)): print('NO Duplicate')
else: print('Duplicate')