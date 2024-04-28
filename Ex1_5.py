class MyInt:
    def __init__(self,value):
        self.value = value
        self.roman_dict = {
            "M" : 1000,
            "CM" : 900,
            "D" : 500,
            "CD" : 400,
            "C" : 100,
            "XC" : 90,
            "L" : 50,
            "XL" : 40,
            "X" : 10,
            "IX" : 9,
            "V" : 5,
            "IV" : 4,
            "I" : 1,
        }
        self.roman = ''
    
    def toRoman(self):
        number = self.value
        while number != 0:
            for x,y in self.roman_dict.items():
                while number >= y:
                    number = number-y
                    self.roman += x
        return self.roman
    
    def __add__(self,b):
        return ((self.value + b.value)*3)/2
    
print(' *** class MyInt ***')
a, b = list(map(int,input('Enter 2 number : ').split()))
value1 = MyInt(a)
value2 = MyInt(b)
print(f'{a} convert to Roman : {value1.toRoman()}')
print(f'{b} convert to Roman : {value2.toRoman()}')
print(f'{a} + {b} = {int(value1+value2)}')