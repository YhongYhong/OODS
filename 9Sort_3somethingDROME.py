def checkDrome(s):
    og = s.copy()
    M_N = s.copy()
    N_M = bubbleLtoB(s)
    bubbleBtoL(M_N)
    if og == N_M and not isRepeated(og):
        print("Metadrome")
    elif og.count(og[0]) == len(og):
        print("Repdrome")
    elif og == N_M and isRepeated(og):
        print("Plaindrome")
    elif og == M_N and not isRepeated(og):
        print("Katadrome")
    elif og == M_N and isRepeated(og):
        print("Nialpdrome")
    else:
        print("Nondrome")
 
def bubbleLtoB(l):
    for last in range(len(l)-1, 0, -1):
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break
    return l

def bubbleBtoL(l):
    for last in range(len(l)-1, 0, -1):
        swaped = False
        for i in range(last):
            if l[i] < l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break
    return l

def isRepeated(l):
    for i in l:
        if l.count(i) > 1: return True
    return False

inp = input("Enter Input : ")
l = [int(i) for i in inp]
checkDrome(l)