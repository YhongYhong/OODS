print('*** multiplication or sum ***')
inp = list(map(int,input('Enter num1 num2 : ').split()))
ans = inp[0] * inp[1]

if ans > 1000: print(f'The result is {inp[0]+inp[1]}')
else: print(f'The result is {ans}')