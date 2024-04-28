def power(a, b):
    if b == 0:
        return 1
    else:
        return a*(power(a, b-1))

inp = list(map(int, input("Enter Input a b : ").split(' ')))

print(power(inp[0], inp[1]))