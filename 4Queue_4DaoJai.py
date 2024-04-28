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
    
def NumtoAct(list):
    b = Queue()
    c = ''
    act = ['Eat', 'Game', 'Learn', 'Movie']
    place = ['Res.', 'ClassR.', 'SuperM.', 'Home']
    for i in list.items:
        newlist = act[int(i[0])] + ':' + place[int(i[2])]
        b.enQueue(newlist)
    for i in range(len(b.items)):
        if i != len(b.items)-1: c += b.items[i] + ', '
        else: c += b.items[i]
    return c

def CalScore(list1, list2):
    point = 0
    for i in range(len(list1.items)):
        a = list1.deQueue()
        b = list2.deQueue()
        if a[0] == b[0] and a[2] == b[2]: point += 4
        elif a[0] == b[0] and a[2] != b[2]: point += 1
        elif a[0] != b[0] and a[2] == b[2]: point += 2
        else: point -= 5
    if point >= 7:
        return "Yes! You're my love! : Score is " + str(point) + "."
    elif point < 7 and point > 0:
        return "Umm.. It's complicated relationship! : Score is " + str(point) + "."
    else:
        return "No! We're just friends. : Score is " + str(point) + "."
    
inp = input('Enter Input : ').split(',')
myq = [x for x in [i[0:3] for i in inp]]
urq = [x for x in [i[4:7] for i in inp]]
my_q = Queue(myq)
ur_q = Queue(urq)

print('My   Queue = ',end='')
for x in range(len(myq)):
    if x != len(myq)-1:
        print(myq[x],end=', ')
    else:
        print(myq[x])
        
print('Your Queue = ',end='')
for x in range(len(urq)):
    if x != len(urq)-1:
        print(urq[x],end=', ')
    else:
        print(urq[x])
        
print(f'My   Activity:Location = {NumtoAct(my_q)}')
print(f'Your Activity:Location = {NumtoAct(ur_q)}')
print(CalScore(my_q, ur_q))
# print(myq ,my_queue.items)