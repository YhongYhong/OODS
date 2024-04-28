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

inp = input('Enter people and time : ').split()
a = [x for x in inp[0]]
main = Queue(a)
cashier1 = Queue()
cashier2 = Queue()
min1 = 0
min2 = 0
# print(main.items)
for i in range(int(inp[1])):
    print(f'{i+1} ',end='')
    if not main.isEmpty():
        b = main.deQueue()
        print(main.items,end=' ')
        
        if cashier1.size() < 5:
            cashier1.enQueue(b)
            b = None
        if not cashier1.isEmpty():
            if min1 % 3 == 0 and min1 != 0:
                cashier1.deQueue()
                if cashier1.size() < 5 and b != None:
                    cashier1.enQueue(b)
                    b = None
            min1 += 1
        if cashier1.size() >= 5 and cashier2.size() < 5 and b != None:
            cashier2.enQueue(b)
        if not cashier2.isEmpty():
            if min2 % 2 == 0 and min2 != 0:
                cashier2.deQueue()
            min2 += 1

        print(cashier1.items, cashier2.items)
    else:
        b = None
        print('[] ',end='')
        if cashier1.size() < 5 and b != None:
            cashier1.enQueue(b)
            b = None
        if not cashier1.isEmpty():
            if min1 % 3 == 0 and min1 != 0:
                cashier1.deQueue()
                if cashier1.size() < 5 and b != None:
                    cashier1.enQueue(b)
                    b = None
            min1 += 1
        if cashier1.size() >= 5 and cashier2.size() < 5 and b != None:
            cashier2.enQueue(b)
        if not cashier2.isEmpty():
            if min2 % 2 == 0 and min2 != 0:
                cashier2.deQueue()
            min2 += 1

        print(cashier1.items, cashier2.items)