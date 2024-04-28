class Monkey:
    def __init__(self, name, strength, intelligence, agility, id):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = id
        
    def getAtt(self, a):
        if a == 'name': return str(self.name)
        elif a == 'str': return int(self.str)
        elif a == 'int': return int(self.int)
        elif a == 'agi': return int(self.agi)
        elif a == 'id' : return int(self.id)
        
    def __repr__(self) -> str:
        return f'{self.id}-{self.name}'
        
def mergeSort(l, left, right, priority, order):
    center = (left+right)//2
    if left < right:
        mergeSort(l, left, center, priority, order)
        mergeSort(l, center+1, right, priority, order)
        merge(l, left, center+1, right, priority, order)
        
def merge(l, left, right, rightEnd, priority, order):
    start = left
    leftEnd = right-1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if compare(l[left], l[right], priority, order):
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
            
    while left <= leftEnd:
        result.append(l[left])
        left += 1
    while right <= rightEnd:
        result.append(l[right])
        right += 1
        
    for ele in result:
        l[start] = ele
        start += 1
        if start > rightEnd:
            break
    
def compare(a,b,priority,order):
    n = len(priority)
    for i in range(n):
        if order == 'D':
            if a.getAtt(priority[i]) > b.getAtt(priority[i]):
                return True
            elif a.getAtt(priority[i]) < b.getAtt(priority[i]):
                return False
            else:
                if priority[i] == 'name':
                    if a.getAtt(priority[i]) > b.getAtt(priority[i]):
                        return True
                    elif a.getAtt(priority[i]) < b.getAtt(priority[i]):
                        return False
        elif order == 'A':
            if a.getAtt(priority[i]) > b.getAtt(priority[i]):
                return False
            elif a.getAtt(priority[i]) < b.getAtt(priority[i]):
                return True
            else:
                if priority[i] == 'name':
                    if a.getAtt(priority[i]) > b.getAtt(priority[i]):
                        return False
                    elif a.getAtt(priority[i]) < b.getAtt(priority[i]):
                        return True
        if i == n-1:
            if a.getAtt('id') < b.getAtt('id'):
                return True
            elif a.getAtt('id') > b.getAtt('id'):
                return False
    return True

type, att_priority, monkey = input("Enter Input: ").split('/')
att_priority = att_priority.split(',')
monkey = monkey.split(',')
monkey_list = []

for o,m in list(enumerate(monkey)):
    m = m.split()
    monkey_list.append(Monkey(m[0], m[1], m[2], m[3], o))
if att_priority[0] != '':
    mergeSort(monkey_list, 0, len(monkey_list)-1, att_priority, type)
print(monkey_list)