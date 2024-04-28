def infix_to_postfix(a):
    operator = ['+', '-', '*', '/', '^']
    parenthesis = ['(', ')']
    stack = []
    ans = ''
    
    for i in range(len(a)):
        if a[i] not in operator and a[i] not in parenthesis:
            ans += a[i]
                    
        elif a[i] in parenthesis:
            if a[i] == '(':
                stack.append(a[i])
            elif a[i] == ')':
                while '(' in stack:
                    if stack[len(stack)-1] == '(':  # เอาวงเล็บออก
                        stack.pop(len(stack)-1)
                        if len(stack) != 0 and (stack[len(stack)-1] == '^'): # ถ้าหลังเอาวงเล็บออกแล้วมีเครื่องหมาย
                            ans += stack.pop()
                        break
                    ans += stack.pop()
        
        elif a[i] in operator:
            if len(stack) != 0:
                if a[i] == '+' or a[i] == '-':
                    while len(stack) != 0 and stack[len(stack)-1] != '(':
                        ans += stack.pop()
                elif a[i] == '*' or a[i] == '/':
                    if stack[len(stack)-1] == '*' or stack[len(stack)-1] == '/' or stack[len(stack)-1] == '^':
                        ans += stack.pop()
                elif a[i] == '^':
                    if stack[len(stack)-1] == '^':
                        ans += stack.pop()
            stack.append(a[i])
    
    while len(stack) != 0:
            ans += stack.pop()
            
    return ans
        

infix = input('Enter Infix : ')
print(f'Postfix : {infix_to_postfix(infix)}')