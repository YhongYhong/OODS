def Pld_check(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return Pld_check(s[1:-1])
        else:
            return False

inp = input("Enter Input : ")

if Pld_check(inp):
    print("'{}' is palindrome".format(inp))
else:
    print("'{}' is not palindrome".format(inp))