def harmonicSum(n):
    if n == 1:
        return 1
    
    return 1/n + harmonicSum(n-1)

def reverse(s):
    if len(s) == 1:
        return s
    
    return s[-1] + reverse(s[:-1])

# inp = int(input("Number : "))     # for harmonicSum method
# print("Answer is : ",end = '')
# print("%.4f" % harmonicSum(inp))

# inp = input("String : ")          # for reverse method
# print(reverse(inp))