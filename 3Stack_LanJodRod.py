class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def push(self, i):
        self.items.append(i)
        
    def pop(self):
        return self.items.pop()
    
    def remove(self, i):
        self.items.remove(i)
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

print('******** Parking Lot ********')
inp = input('Enter max of car,car in soi,operation : ').split()
count = inp[1].split(',')
car = Stack()

for i in range(len(count)):
    if count[i] != '0':
        car.push(int(count[i]))

if inp[2] == 'arrive':
    # print(inp[0], car.size())
    if int(inp[3]) in car.items:
        print(f'car {inp[3]} already in soi')
    elif int(inp[0]) == car.size():
        print(f'car {inp[3]} cannot arrive : Soi Full')
    elif int(inp[0]) > car.size():
        print(f'car {inp[3]} arrive! : Add Car {inp[3]}')
        car.push(int(inp[3]))
elif inp[2] == 'depart':
    if int(inp[3]) in car.items:
        print(f'car {inp[3]} depart ! : Car {inp[3]} was remove')
        car.remove(int(inp[3]))
    elif car.isEmpty():
        print(f'car {inp[3]} cannot depart : Soi Empty')
    elif int(inp[3]) not in car.items:
        print(f'car {inp[3]} cannot depart : Dont Have Car {inp[3]}')
        
print(car.items)