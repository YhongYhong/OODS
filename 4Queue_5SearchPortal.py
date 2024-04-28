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
        return self.items == []
    
    def size(self):
        return len(self.items)
    
def map_checker(w, h, m):
    have_f = False
    for i in m:
        if len(i) != w or len(m) != h:
            return False
        if 'F' in i: 
            have_f = True
        
    if not have_f: 
        return False
    else: 
        return True

def search_portal(w, h, m):
    if map_checker(w, h, m): pass
    else: return print('Invalid map input.')
    
    past = Queue()
    q = Queue()
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == 'F':
                width = x
                height = y
                print(f'Queue: [{(x, y)}]')
            elif m[y][x] == 'O':
                portal = (x, y)
    
    while True:
        if height-1 >= 0 and m[height-1][width] in '_O' and (width, height-1) not in past.items:
            lo = (width, height-1)
            past.enQueue(lo)
            q.enQueue(lo)
        elif width+1 < w and m[height][width+1] in '_O' and (width+1 ,height) not in past.items:
            lo = (width+1, height)
            past.enQueue(lo)
            q.enQueue(lo)
        elif height+1 < h and m[height+1][width] in '_O' and (width, height+1) not in past.items:
            lo = (width, height+1)
            past.enQueue(lo)
            q.enQueue(lo)
        elif width-1 >= 0 and m[height][width-1] in '_O' and (width-1, height) not in past.items:
            lo = (width-1, height)
            past.enQueue(lo)
            q.enQueue(lo)
        else:
            if q.isEmpty():
                return print('Cannot reach the exit portal.')
            elif portal in q.items:
                return print('Found the exit portal.')
            print(f'Queue: {q.items}')
            lo = q.deQueue()
            width = lo[0]
            height = lo[1]
    
inp = input('Enter width, height, and room: ').split(' ')
m = inp[2].split(',')

search_portal(int(inp[0]), int(inp[1]), m)