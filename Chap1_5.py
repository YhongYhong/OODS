print('*** Fun with countdown ***')
inp = list(map(int,input('Enter List : ').split()))
cd_list = [[0],[]]
order = 0
temp = 0
list = []
stack = []

for i in inp:
    if temp-i == 1:
        if stack == []:
            stack = [temp, i]
            cd_list[1].append(list)
            if i == 1:
                if cd_list[1][order] == []:
                    cd_list[1][order] = stack
                stack = []
                order+=1
                cd_list[0] = order
        elif i == 1 :
            stack.append(i)
            if cd_list[1][order] == []:
                cd_list[1][order] = stack
            stack = []
            order+=1
            cd_list[0] = order
        else: stack.append(i)
    elif i == 1:
        stack = [i]
        cd_list[1].append(list)
        cd_list[1][order] = stack
        order+=1
        cd_list[0] = order
    else: stack = []
    temp = i
    
print(f'{cd_list}')
    
