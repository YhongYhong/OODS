def print1ToN(n):
    if n <= 1:
        print(1,end= ' ')
    else:
        print1ToN(n-1)
        print(n,end=' ')

def printNto1(n):
    if n <= 1:
        print(1)
    else:
        print(n,end=' ')
        n -= 1
        printNto1(n)

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)