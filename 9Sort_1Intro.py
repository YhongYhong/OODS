def selection(l):
    for last in range(len(l)-1, 0, -1):
        # print((l[last]), l[0])
        biggest = l[0]
        biggest_i = 0
        print(biggest)
        for i in range(1, last+1):
            if int(l[i]) > int(biggest):
                biggest = l[i]
                biggest_i = i
        l[last], l[biggest_i] = str(l[biggest_i]), l[last]
    return l

inp = input("Enter Input : ").split()
og = inp.copy()
selection(inp)
print(inp)
print('Yes' if inp == og else 'No')