def grouping(s, pin):
    if pin >= 1 and s[pin-1] == s[pin-2]:
        return grouping(s, pin-1)
    else:
        return counting(s, pin)

def counting(s, pin):
    if pin == len(s)-1 or s[pin-1] != s[pin]:
        return 1
    else:
        return counting(s, pin+1) + 1

inp = input("input number : ").split(",")
count = 0
if inp[0] == '':
    print("Output : List is entry")
elif int(inp[1]) >= len(inp[0]):
    print("Output : Pin number out of range")
elif int(inp[1]) < 1:
    print("Output : Pin number less than 1")
else:
    print("Character :", inp[0][int(inp[1])-1])
    print("Count :",grouping(inp[0], int(inp[1])))