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
    
class StackCalc:
    def __init__(self):
        self.value = 0
        self.stack = Stack()
    
    def run(self,arg):
        for i in range(len(arg)):
            if arg[i] in '+-*/':
                prev1 = self.stack.pop()
                prev2 = self.stack.pop()
                if arg[i] == '+': result = self.to_plus(prev1, prev2)
                elif arg[i] == '-': result = self.to_minus(prev1, prev2)
                elif arg[i] == '*': result = self.to_multiply(prev1, prev2)
                elif arg[i] == '/': result = self.to_divide(prev1, prev2)
                self.stack.push(int(result))
            elif arg[i] == 'DUP':
                self.stack.push(self.stack.peek())
            elif arg[i] == 'POP':
                self.stack.pop()
            elif arg[i] == 'PSH':
                pass
            elif arg[i].isnumeric():
                self.stack.push(int(arg[i]))
            else:
                self.value = 'Invalid instruction: ' + arg[i]
                return self.value
        
        if self.stack.size() != 0:
            self.value = self.stack.pop()
            return self.value 
        else:
            return self.value
        
    
    def to_plus(self, one, two):
        return int(one) + int(two)
    
    def to_minus(self, one, two):
        return int(one) - int(two)
    
    def to_multiply(self, one, two):
        return int(one) * int(two)
    
    def to_divide(self, one, two):
        return int(one) / int(two)
    
    def getValue(self):
        return self.value
    

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())