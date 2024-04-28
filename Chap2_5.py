print('*** TorKham HanSaa ***')
inp = input('Enter Input : ').split(',')
lst = []
last_word = ''

for i in inp:
    if i[:2] == 'P ' and i != last_word:
        # print(f'{last_word[-2:]} , {i[2:4]}')
        if last_word[-2:].lower() == i[2:4].lower() or last_word == '':
            lst.append(i[2:])
            print(f"'{i[2:]}' -> {lst}")
        else: print(f"'{i[2:]}' -> game over")
        last_word = i
    elif i[0] == 'R':
        lst = []
        last_word = ''
        print('game restarted')
    elif i[0] == 'X':
        break
    else:
        print(f"'{i}' is Invalid Input !!!")
        break
    
    