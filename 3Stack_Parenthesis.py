inp = input('Enter expresion : ')
stack = []
open = ['{', '[', '(']
close = ['}', ']', ')']

for i in range(len(inp)):
    if i == len(inp)-1 and len(stack) != 0 and inp[i] not in close:
        if inp[i] in open:
            stack.append(inp[i])
        print(f'{inp} open paren excess   {len(stack)} : ',end='')
        for i in stack:
            print(i,end='')
        
    elif inp[i] in open:
        stack.append(inp[i])
        
    elif inp[i] in close:
        pos = close.index(inp[i])
        if len(stack) > 0 and stack[len(stack)-1] == open[pos]:
            stack.pop()
            if len(stack) == 0 and i == len(inp)-1: print(f'{inp} MATCH')
        elif len(stack) == 0:
            print(f'{inp} close paren excess')
            break
        else: 
            print(f'{inp} Unmatch open-close')
            break