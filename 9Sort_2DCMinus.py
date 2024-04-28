def selection(l):
    for last in range(len(l)-1, 0, -1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1, last+1):
            if int(l[i]) > int(biggest):
                biggest = l[i]
                biggest_i = i
        if int(l[last]) >= 0:
            l[last], l[biggest_i] = str(l[biggest_i]), l[last]
    return l

inp = input("Enter Input : ").split()
selection(inp)
for i in inp: print(i,end=' ')