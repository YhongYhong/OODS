def mod_position(arr, s):
    lst = []
    i = 2
    pos = s
    while len(arr)-pos >= 0:
        lst.append(arr[pos-1])
        pos = s*i
        i+=1
    return lst

print('*** Mod Position ***')
alp,num = input('Enter Input : ').split(',')
print(mod_position(alp,int(num)))