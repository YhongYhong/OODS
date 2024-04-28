print('*** Fun with Drawing ***')
inp = int(input('Enter input : '))
row = 1
column = 1
head1 = inp
head2 = inp
head3 = (inp*3)-2
head4 = (inp*3)-2

while row <= (inp*2)+(inp-2):
    while column <= ((inp*2)+(inp-2))+(inp-1):
        if column == head1 or column == head2 or column == head3 or column == head4:
            print('*',end='')
        elif ((column > head1 and column < head2) or (column > head3 and column < head4)) and head2 != 0:
            print('+',end='')
        elif head2 == 0 and column > head1 and column < head4:
            print('+',end='')
        else: print('.',end='')
        column+=1
    print('')
    column = 1
    if row < inp:
        head1 = head1-1
        head2 = head2+1
        head3 = head3-1
        head4 = head4+1
    else:
        head1 = head1+1
        head2 = 0
        head3 = 0
        head4 = head4-1
    row+=1