print('*** String Rotation ***')
first, second = input('Enter 2 strings : ').split()
r_first = first
r_second = second
status = False
i = 0

while status != True:
    i+=1
    first = first[-2:] + first[:-2]
    second = second[3:] + second[:3]
    if i <= 5:
        print(f'{i} {first} {second}')
    if first == r_first and second == r_second:
        status = True

if i > 5:
    print(' . . . . . ')
    print(f'{i} {first} {second}')
print(f'Total of  {i} rounds.')