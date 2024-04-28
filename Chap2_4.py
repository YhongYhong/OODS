def t_to_f(z):
    lst = []
    stack = []
    num1 = 0
    num2 = 0
    num3 = 0
    if len(z) < 3:
        return f'Array Input Length Must More Than 2'
    for a in z:
        num2=0
        for b in z:
            num3=0
            for c in z:
                if (a+b+c == 5 and a<=b<=c) and (num2 != num1 and num2 != num3 and num1 != num3):
                    stack = [a, b, c]
                    if lst != []:
                        can = True
                        for i in range(len(lst)):
                            if [a,b,c]==lst[i] or [a,c,b]==lst[i] or [b,a,c]==lst[i] or [b,c,a]==lst[i] or [c,a,b]==lst[i] or [c,b,a]==lst[i]:
                                can = False
                        if can == True : lst.append(stack)
                    elif lst == []: lst.append(stack)
                    stack = []
                num3+=1
            num2+=1
        num1+=1
    return lst

num = list(map(int,input('Enter Your List : ').split()))
print(t_to_f(num))