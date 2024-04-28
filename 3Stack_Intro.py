inp = input('Enter Input : ').split(',')
stack = []

for i in range(len(inp)):
    if inp[i][0] == 'A':
        stack.append(inp[i][2:])
        print(f'Add = {inp[i][2:]} and Size = {len(stack)}')
    elif inp[i][0] == 'P':
        if len(stack) == 0:
            print('-1')
        else:
            print(f'Pop = {stack.pop()} and Index = {(len(stack))}')
    
if len(stack) == 0:
    print(f'Value in Stack = Empty')
else : 
    print(f'Value in Stack = ',end = '')
    for i in stack:
        print(i,end=' ')