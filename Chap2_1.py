class translator:
    def __init__(self):
        self.roman = {
            'M':1000,
            'CM':900,    
            'D':500,    
            'CD':400,
            'C':100,    
            'XC':90,    
            'L':50,    
            'XL':40,
            'X':10,    
            'IX':9,    
            'V':5,    
            'IV':4,    
            'I':1,
        }
        
    def deciToRoman(self, num):
        roman = ''
        for x,y in self.roman.items():
            while num >= y:
                num = num-y
                roman+=x
        return roman

    def romanToDeci(self, s):
        number = 0
        prev_num = 1001
        for i in s:
            for x,y in self.roman.items():
                if i == x:
                    if prev_num < y: 
                        y=(y-prev_num*2)
                    number+=y
                    prev_num = y
                    s = s[1:]  
        return number
                    

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))