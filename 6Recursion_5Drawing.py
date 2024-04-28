def staircase(n, t):
    if n % abs(t) == 0 and n <= abs(t)*(abs(t)-1):
        print()
    if n != 1:
        if n <= t or (n % t <= (t-(n//t)) and n % t != 0):
            print("#",end='')
        elif t < 0 and n > abs(t)*(abs(t)-1) :
            print("#",end='')
        else:
            print("_",end='')
        return staircase(n-1, t)
    else:
        return ("#")
    
inp = int(input("Enter Input : "))
c = inp*inp
if inp == 0:
    print("Not Draw!")
else:
    print(staircase(c, inp))

# 1 == 1
# 2 == 3|2,1
# 3 == 7|5,4|3,2,1
# 4 == 13|10,9|7,6,5|4,3,2,1
# 5 == 21|17,16|13,12,11|9,8,7,6|5,4,3,2,1