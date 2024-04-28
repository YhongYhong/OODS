print('*** Reading E-Book ***')
text, hl = input('Text , Highlight : ').split(",")

for i in text:
    if i == hl:
        print(f'[{i}]',end='')
    else: print(i,end='')